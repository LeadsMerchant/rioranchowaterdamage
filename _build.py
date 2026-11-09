#!/usr/bin/env python3
"""Generate the static site pages for rioranchowaterdamage.com"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PHONE_DISP = "{{PHONE}}"
PHONE_TEL = "{{PHONE_TEL}}"

def nav(active=""):
    items = [
        ("index.html", "Home", "home"),
        ("water-damage-restoration.html", "Water Damage", "water"),
        ("flood-cleanup.html", "Flood Cleanup", "flood"),
        ("burst-pipe-leak.html", "Burst Pipes", "burst"),
        ("mold-remediation.html", "Mold", "mold"),
        ("service-areas.html", "Service Areas", "areas"),
        ("about.html", "About", "about"),
        ("contact.html", "Contact", "contact"),
    ]
    links = []
    for href, label, key in items:
        cur = ' aria-current="page"' if key == active else ""
        links.append(f'<a href="{href}"{cur}>{label}</a>')
    return "\n          ".join(links)

def head(title, description, canonical, extra_schema="", active=""):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://rioranchowaterdamage.com/{canonical}">
  <meta name="robots" content="index, follow">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://rioranchowaterdamage.com/{canonical}">
  <meta property="og:locale" content="en_US">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="css/styles.css">
{extra_schema}</head>
'''

def header(active=""):
    return f'''<body>
  <div class="topbar">
    Free referral for Rio Rancho homeowners &nbsp;·&nbsp;
    <a href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a>
  </div>
  <header class="site-header">
    <div class="container header-inner">
      <a class="logo" href="index.html">
        <span class="logo-mark" aria-hidden="true">💧</span>
        <span>Rio Rancho Water Damage<small>Local referral connection</small></span>
      </a>
      <nav class="nav" aria-label="Main">
          {nav(active)}
        <a class="btn btn-primary header-cta" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a>
      </nav>
    </div>
  </header>
'''

def footer():
    return f'''  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="footer-brand">Rio Rancho Water Damage</div>
          <p>A free referral service that helps homeowners in Rio Rancho and nearby communities connect with independent, licensed water damage and mold remediation providers.</p>
          <p><a class="phone-link" href="tel:{PHONE_TEL}" style="color:#5eead4">{PHONE_DISP}</a></p>
        </div>
        <div>
          <h3>Services</h3>
          <ul>
            <li><a href="water-damage-restoration.html">Water Damage Restoration</a></li>
            <li><a href="flood-cleanup.html">Flood Cleanup</a></li>
            <li><a href="burst-pipe-leak.html">Burst Pipe &amp; Leak Damage</a></li>
            <li><a href="mold-remediation.html">Mold Remediation</a></li>
          </ul>
        </div>
        <div>
          <h3>Info</h3>
          <ul>
            <li><a href="service-areas.html">Service Areas</a></li>
            <li><a href="about.html">About</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="privacy.html">Privacy Policy</a></li>
            <li><a href="terms.html">Terms of Use</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-disclosure">
        <strong>Important:</strong> This site is a free referral service. Calls may be forwarded to an independent, licensed service provider in your area. We do not perform restoration work ourselves, and we are not affiliated with any single contractor. Always confirm licensing, insurance, and pricing directly with the provider you speak with.
      </div>
      <div class="footer-bottom">
        <span>&copy; 2026 Rio Rancho Water Damage Referral. All rights reserved.</span>
        <span><a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a></span>
      </div>
    </div>
  </footer>
  <div class="mobile-callbar" aria-label="Call now">
    <a href="tel:{PHONE_TEL}">📞 Call Now — {PHONE_DISP}</a>
  </div>
</body>
</html>
'''

# ---------- PAGE CONTENTS ----------

website_schema = '''  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Rio Rancho Water Damage",
    "url": "https://rioranchowaterdamage.com/",
    "description": "Free referral service connecting Rio Rancho, NM homeowners with independent water damage and mold remediation providers.",
    "potentialAction": {
      "@type": "CommunicateAction",
      "name": "Call for referral"
    }
  }
  </script>
'''

faq_schema = '''  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Is this a water damage restoration company?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. This website is a free referral service. When you call, we help connect you with an independent, licensed provider who can discuss your water damage or mold situation."
        }
      },
      {
        "@type": "Question",
        "name": "What areas near Rio Rancho do you cover?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "We focus on Rio Rancho and nearby communities including Corrales, Bernalillo, Placitas, and Northwest Albuquerque. Availability depends on the providers in our network at the time you call."
        }
      },
      {
        "@type": "Question",
        "name": "What kinds of water problems can I call about?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Homeowners commonly call about storm or monsoon flooding, burst pipes, slab leaks, water heater failures, evaporative cooler issues, sewage backups, and secondary mold concerns after water intrusion."
        }
      },
      {
        "@type": "Question",
        "name": "Will I be charged for calling?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "There is no charge to call this referral line. Any fees for inspection or restoration work are between you and the independent provider you choose to hire."
        }
      },
      {
        "@type": "Question",
        "name": "Should I call my insurance company first?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "If you have homeowners insurance and the damage may be covered, it is often wise to document the situation and contact your insurer. A restoration provider can also walk you through typical next steps for your type of loss."
        }
      },
      {
        "@type": "Question",
        "name": "What should I do while I wait for help?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "If it is safe, shut off the water source, avoid electrical hazards, move valuables out of wet areas, and photograph the damage. Do not enter standing water if you suspect electrical risk or sewage contamination."
        }
      }
    ]
  }
  </script>
'''

pages = {}

# HOME
pages["index.html"] = (
    head(
        "Rio Rancho Water Damage Help | Free Local Referral",
        "Need water damage or mold help in Rio Rancho, NM? Call our free referral line to connect with independent local restoration providers.",
        "",
        website_schema + faq_schema,
    )
    + header("home")
    + f'''  <main>
    <section class="hero">
      <div class="container hero-grid">
        <div>
          <div class="hero-badge">Rio Rancho · Corrales · Bernalillo · NW Albuquerque</div>
          <h1>Water damage in Rio Rancho? Get connected to local help.</h1>
          <p class="lead">We are a free referral service for homeowners dealing with flooding, burst pipes, leaks, and mold concerns. Call and we will help connect you with an independent, licensed provider in your area.</p>
          <div class="hero-actions">
            <a class="btn btn-primary btn-lg" href="tel:{PHONE_TEL}">📞 Call {PHONE_DISP}</a>
            <a class="btn btn-secondary btn-lg" href="water-damage-restoration.html">See how it works</a>
          </div>
          <p class="hero-note">No charge to call. You speak with a real provider about your situation. We do not perform restoration work ourselves.</p>
        </div>
        <aside class="hero-card" aria-label="Common reasons to call">
          <h2>Common reasons homeowners call</h2>
          <ul>
            <li>Monsoon or storm water entered the home</li>
            <li>Burst pipe, slab leak, or water heater failure</li>
            <li>Standing water in basement, crawl space, or rooms</li>
            <li>Musty smell or visible mold after a leak</li>
            <li>Need guidance before or after calling insurance</li>
          </ul>
        </aside>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2>How this referral works</h2>
          <p>Simple steps. Clear expectations. No pressure.</p>
        </div>
        <div class="steps">
          <div class="step">
            <h3>Call the number</h3>
            <p>Tell us what happened — flooding, a burst pipe, a slow leak, or mold after water damage. Share your location in or near Rio Rancho.</p>
          </div>
          <div class="step">
            <h3>Get connected</h3>
            <p>We help connect you with an independent provider who handles water damage restoration or mold remediation in the area.</p>
          </div>
          <div class="step">
            <h3>Talk through next steps</h3>
            <p>Ask about inspection, drying, cleanup, and documentation. Hiring decisions and pricing are always between you and the provider.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="section-head">
          <h2>Services we can refer you for</h2>
          <p>Water emergencies and related mold concerns for Rio Rancho-area homes.</p>
        </div>
        <div class="card-grid card-grid-2">
          <article class="card">
            <div class="icon" aria-hidden="true">🌊</div>
            <h3>Water Damage Restoration</h3>
            <p>Help after leaks, appliance failures, and indoor water intrusion — extraction, drying, and cleanup guidance.</p>
            <a class="more" href="water-damage-restoration.html">Learn more →</a>
          </article>
          <article class="card">
            <div class="icon" aria-hidden="true">🌧️</div>
            <h3>Flood Cleanup</h3>
            <p>Support after storm water, monsoon runoff, or other flooding that soaked floors, walls, or belongings.</p>
            <a class="more" href="flood-cleanup.html">Learn more →</a>
          </article>
          <article class="card">
            <div class="icon" aria-hidden="true">🔧</div>
            <h3>Burst Pipe &amp; Leak Damage</h3>
            <p>Broken pipes, slab leaks, and supply-line failures can soak structure fast. Get connected for assessment and drying.</p>
            <a class="more" href="burst-pipe-leak.html">Learn more →</a>
          </article>
          <article class="card">
            <div class="icon" aria-hidden="true">🦠</div>
            <h3>Mold Remediation</h3>
            <p>When moisture lingers, mold can follow. We refer callers seeking mold cleanup tied to water intrusion.</p>
            <a class="more" href="mold-remediation.html">Learn more →</a>
          </article>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2>Why Rio Rancho homeowners deal with water damage</h2>
          <p>Local conditions create real moisture risks — even in a dry climate.</p>
        </div>
        <div class="card-grid card-grid-3">
          <div class="card">
            <h3>Monsoon season storms</h3>
            <p>Summer monsoon rains can overwhelm drainage, push water under doors, or leak through roofs and windows during intense downpours.</p>
          </div>
          <div class="card">
            <h3>Winter freezes</h3>
            <p>Cold snaps can freeze exposed or poorly insulated pipes. When they thaw, bursts can flood cabinets, walls, and floors.</p>
          </div>
          <div class="card">
            <h3>Swamp / evaporative coolers</h3>
            <p>Evaporative coolers are common in New Mexico. Overflows, clogged drains, or pad issues can drip water into attics and living spaces.</p>
          </div>
          <div class="card">
            <h3>Water heater failures</h3>
            <p>Aging tanks and supply connections can fail without much warning, dumping gallons into utility rooms and nearby floors.</p>
          </div>
          <div class="card">
            <h3>Slab leaks</h3>
            <p>Pipes under concrete slabs can develop hidden leaks. Soft floors, unexplained high water bills, or warm spots may be early signs.</p>
          </div>
          <div class="card">
            <h3>Secondary mold growth</h3>
            <p>Any unresolved moisture — from a slow leak or incomplete drying — can lead to musty odors and mold on porous materials.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="section-head">
          <h2>Areas we focus on</h2>
          <p>Rio Rancho and nearby Sandoval County / Northwest Albuquerque communities.</p>
        </div>
        <ul class="area-list">
          <li>Rio Rancho</li>
          <li>Corrales</li>
          <li>Bernalillo</li>
          <li>Placitas</li>
          <li>Northwest Albuquerque</li>
          <li>Northern Meadows</li>
          <li>Cabezon</li>
          <li>Enchanted Hills</li>
        </ul>
        <p><a href="service-areas.html">Full service area details →</a></p>
      </div>
    </section>

    <section class="section" id="faq">
      <div class="container">
        <div class="section-head">
          <h2>Frequently asked questions</h2>
        </div>
        <div class="faq">
          <details>
            <summary>Is this a water damage restoration company?</summary>
            <p>No. This website is a free referral service. When you call, we help connect you with an independent, licensed provider who can discuss your water damage or mold situation.</p>
          </details>
          <details>
            <summary>What areas near Rio Rancho do you cover?</summary>
            <p>We focus on Rio Rancho and nearby communities including Corrales, Bernalillo, Placitas, and Northwest Albuquerque. Availability depends on the providers in our network at the time you call.</p>
          </details>
          <details>
            <summary>What kinds of water problems can I call about?</summary>
            <p>Homeowners commonly call about storm or monsoon flooding, burst pipes, slab leaks, water heater failures, evaporative cooler issues, sewage backups, and secondary mold concerns after water intrusion.</p>
          </details>
          <details>
            <summary>Will I be charged for calling?</summary>
            <p>There is no charge to call this referral line. Any fees for inspection or restoration work are between you and the independent provider you choose to hire.</p>
          </details>
          <details>
            <summary>Should I call my insurance company first?</summary>
            <p>If you have homeowners insurance and the damage may be covered, it is often wise to document the situation and contact your insurer. A restoration provider can also walk you through typical next steps for your type of loss.</p>
          </details>
          <details>
            <summary>What should I do while I wait for help?</summary>
            <p>If it is safe, shut off the water source, avoid electrical hazards, move valuables out of wet areas, and photograph the damage. Do not enter standing water if you suspect electrical risk or sewage contamination.</p>
          </details>
        </div>
      </div>
    </section>

    <section class="cta-band">
      <div class="container">
        <h2>Ready to talk with someone about your water damage?</h2>
        <p>Call our free Rio Rancho referral line. We will help connect you with an independent local provider.</p>
        <a class="btn btn-primary btn-lg" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a>
      </div>
    </section>
  </main>
'''
    + footer()
)

def service_page(filename, active, title, meta, h1, lead, body, schema_name, schema_desc):
    schema = f'''  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "{schema_name}",
    "serviceType": "{schema_name}",
    "description": "{schema_desc}",
    "provider": {{
      "@type": "Organization",
      "name": "Rio Rancho Water Damage",
      "url": "https://rioranchowaterdamage.com/",
      "description": "Free referral service connecting callers with independent restoration providers."
    }},
    "areaServed": [
      {{"@type": "City", "name": "Rio Rancho", "containedInPlace": {{"@type": "State", "name": "New Mexico"}}}},
      {{"@type": "City", "name": "Corrales"}},
      {{"@type": "City", "name": "Bernalillo"}},
      {{"@type": "Place", "name": "Northwest Albuquerque"}}
    ],
    "url": "https://rioranchowaterdamage.com/{filename}"
  }}
  </script>
'''
    content = (
        head(title, meta, filename, schema)
        + header(active)
        + f'''  <main>
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumb"><a href="index.html">Home</a> / {h1}</p>
        <h1>{h1}</h1>
        <p class="lead">{lead}</p>
      </div>
    </section>
    <section class="section">
      <div class="container content-split">
        <article class="prose">
{body}
          <div class="notice">
            <strong>Referral disclosure:</strong> This site does not perform restoration or mold remediation. We connect callers with independent providers. Confirm licensing, insurance, scope, and pricing directly with any company you hire.
          </div>
        </article>
        <aside>
          <div class="sidebar-card">
            <h2>Need help now?</h2>
            <p>Call our free referral line for Rio Rancho and nearby communities.</p>
            <div class="phone-display"><a class="phone-link" href="tel:{PHONE_TEL}">{PHONE_DISP}</a></div>
            <a class="btn btn-primary btn-block" href="tel:{PHONE_TEL}">Call Now</a>
            <p class="muted" style="margin-top:1rem;margin-bottom:0;font-size:0.85rem;">No charge to call. Work pricing is set by the provider.</p>
          </div>
        </aside>
      </div>
    </section>
    <section class="cta-band">
      <div class="container">
        <h2>Talk with a local provider about your situation</h2>
        <p>Describe what happened. We will help connect you.</p>
        <a class="btn btn-primary btn-lg" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a>
      </div>
    </section>
  </main>
'''
        + footer()
    )
    pages[filename] = content

# Water damage
service_page(
    "water-damage-restoration.html",
    "water",
    "Water Damage Restoration Referral | Rio Rancho, NM",
    "Get connected with independent water damage restoration providers serving Rio Rancho, Corrales, Bernalillo, and NW Albuquerque.",
    "Water Damage Restoration in Rio Rancho",
    "When water gets into your home, acting quickly can limit damage to floors, walls, and belongings. Our free referral line helps Rio Rancho-area homeowners connect with independent restoration providers.",
    f'''          <p>Water damage is stressful whether it started with a sudden pipe break or a slow drip you only noticed after floors felt soft. In Rio Rancho and nearby communities, homeowners also deal with monsoon-driven roof and window leaks, evaporative cooler overflows, and winter freezes that crack pipes. This page explains what restoration typically involves and how our referral service can help you reach someone who does the work.</p>

          <h2>What water damage restoration usually includes</h2>
          <p>Independent restoration companies often start by stopping the source (if it is still active), assessing how far moisture has traveled, and removing standing water. From there, the focus shifts to drying structural materials, cleaning affected areas, and deciding what can be saved versus what needs replacement. The exact steps depend on how clean the water was, how long materials stayed wet, and which parts of the home were hit.</p>
          <p>A typical conversation with a provider may cover:</p>
          <ul>
            <li>Where the water came from and when you first noticed it</li>
            <li>Which rooms, flooring types, and wall materials are wet</li>
            <li>Whether electricity, HVAC, or sewage could be involved</li>
            <li>Photos or a walkthrough to estimate scope</li>
            <li>How documentation for insurance claims usually works</li>
          </ul>

          <h2>Common causes in the Rio Rancho area</h2>
          <p>New Mexico’s climate is dry overall, but that does not protect homes from indoor plumbing failures or intense summer storms. Local triggers we hear about include monsoon downpours that overwhelm gutters, frozen pipes during cold snaps, swamp cooler drain problems, failed water heaters, supply-line breaks under sinks, and slab leaks that go unnoticed until flooring cups or water bills jump.</p>
          <p>If you live in neighborhoods such as Enchanted Hills, Cabezon, Northern Meadows, or closer to Corrales and Bernalillo, the same advice applies: stop the water if you safely can, document what you see, and get a professional assessment before materials sit wet for days.</p>

          <h2>Why drying matters as much as cleanup</h2>
          <p>Removing visible water is only part of the job. Moisture trapped in carpet pad, baseboards, drywall, and subfloors can keep feeding damage — including odors and mold — after the floor looks dry on the surface. Providers use moisture meters, air movers, and dehumidifiers to bring materials back to a safer moisture level. Asking how they will verify dryness is a reasonable question before you authorize work.</p>

          <h2>How our free referral helps</h2>
          <p>We do not send a crew ourselves. When you call <a class="phone-link" href="tel:{PHONE_TEL}">{PHONE_DISP}</a>, we help connect you with an independent, licensed provider who can discuss next steps for your water damage situation. You stay in control of whether to schedule an inspection or hire anyone. There is no fee to use this referral line.</p>

          <h2>Practical steps you can take right away</h2>
          <ol>
            <li>If it is safe, shut off the water supply to the leak or the whole house.</li>
            <li>Avoid standing water near electrical outlets, panels, or appliances.</li>
            <li>Move furniture and valuables out of wet zones when you can do so safely.</li>
            <li>Take clear photos and short videos of affected rooms.</li>
            <li>Note the time the problem started and any recent weather or plumbing work.</li>
            <li>Call for a referral if you want to speak with a restoration provider about options.</li>
          </ol>
          <p>Related pages: <a href="flood-cleanup.html">flood cleanup</a>, <a href="burst-pipe-leak.html">burst pipe and leak damage</a>, and <a href="mold-remediation.html">mold remediation</a>.</p>
''',
    "Water Damage Restoration Referral",
    "Free referral connecting Rio Rancho homeowners with independent water damage restoration providers.",
)

service_page(
    "flood-cleanup.html",
    "flood",
    "Flood Cleanup Referral | Rio Rancho, NM",
    "Flooding from storms or indoor failures? Call our free Rio Rancho referral line to connect with independent flood cleanup providers.",
    "Flood Cleanup Help for Rio Rancho Homes",
    "Storm water, monsoon runoff, or indoor flooding can soak a home in minutes. We help you connect with independent providers who handle flood cleanup and drying.",
    f'''          <p>Flooding does not only mean a river overflowing. For many Rio Rancho homeowners, “flood cleanup” means several inches of water across a garage, living room, or hallway after a fierce monsoon cell, a blocked drain, or a major indoor plumbing failure. Fast removal of water and a careful drying plan are what protect flooring, cabinets, and wall cavities from longer-term damage.</p>

          <h2>Outdoor storms vs. indoor flooding</h2>
          <p>Water that entered from outside — through a door threshold, window well, roof leak during heavy rain, or yard drainage problem — may carry soil and debris. Water from a clean supply line break is different from water that backed up from a drain or sewer. Providers often categorize water by how contaminated it may be, because that affects cleaning methods and what materials can be kept. Be ready to describe the source as clearly as you can.</p>

          <h2>What flood cleanup typically involves</h2>
          <p>After safety checks, cleanup usually starts with extracting standing water, removing unsalvageable porous materials when needed, cleaning hard surfaces, and setting up drying equipment. Belongings may need to be moved, inventoried, or packed out. Some homeowners also need help understanding what insurance may ask for — item lists, moisture readings, and before/after photos.</p>
          <ul>
            <li>Water extraction from floors and low spots</li>
            <li>Assessment of carpet, pad, baseboards, and drywall</li>
            <li>Cleaning and sanitizing appropriate surfaces</li>
            <li>Structural drying with monitored equipment</li>
            <li>Guidance on what to discard vs. attempt to restore</li>
          </ul>

          <h2>Monsoon season considerations</h2>
          <p>Rio Rancho and the greater Albuquerque metro see intense summer storms. Short, heavy rainfall can overwhelm landscaping grades, patio drains, and older window seals. If water entered during a storm, check whether more rain is forecast before you open walls or pull flooring — and ask the provider how they protect the home while drying is underway.</p>
          <p>Homes near arroyos, lower lots, or with below-grade entries can be more exposed when drainage is blocked by debris. Clearing gutters and keeping downspouts directed away from the foundation are useful prevention steps after you stabilize the current problem.</p>

          <h2>Safety first</h2>
          <p>Do not walk through floodwater if you suspect live electricity. Stay out of areas with sewage contamination unless you have proper protection and know what you are doing. If anyone in the home has breathing issues, limit exposure to damp, dusty demolition until the area is properly handled. When in doubt, wait for professional guidance.</p>

          <h2>Call for a flood cleanup referral</h2>
          <p>Our line at <a class="phone-link" href="tel:{PHONE_TEL}">{PHONE_DISP}</a> is a free way to request a connection to an independent flood cleanup / water damage provider serving Rio Rancho and nearby towns. We are not the cleanup company. You decide whether to schedule service after you speak with them.</p>
          <p>Also see <a href="water-damage-restoration.html">water damage restoration</a> and our <a href="service-areas.html">service areas</a>.</p>
''',
    "Flood Cleanup Referral",
    "Free referral for flood cleanup assistance in Rio Rancho, New Mexico.",
)

service_page(
    "burst-pipe-leak.html",
    "burst",
    "Burst Pipe & Leak Water Damage | Rio Rancho Referral",
    "Burst pipe, slab leak, or supply line failure in Rio Rancho? Call for a free referral to independent water damage providers.",
    "Burst Pipe &amp; Leak Water Damage",
    "A broken pipe can release a surprising amount of water in a short time. Get connected with independent providers who assess and dry leak-related damage in the Rio Rancho area.",
    f'''          <p>Burst pipes and hidden leaks are among the most common indoor water emergencies. Supply lines under sinks, toilet connectors, water heaters, washing machine hoses, and pipes in attics or crawl spaces can fail from age, freezing, corrosion, or accidental damage during renovations. In slab-on-grade homes common across New Mexico, leaks under the concrete can be harder to spot until damage spreads.</p>

          <h2>Signs you may have an active leak</h2>
          <ul>
            <li>Sudden drop in water pressure or the sound of running water when fixtures are off</li>
            <li>Warm spots on floors (sometimes associated with hot-water slab leaks)</li>
            <li>Unexplained increase on the water bill</li>
            <li>Soft, staining, or cupping flooring</li>
            <li>Peeling paint, bubbling drywall, or damp baseboards</li>
            <li>Musty odor in a closet, cabinet, or closed room</li>
          </ul>
          <p>If you can locate the shutoff valve, turning off the water can prevent further flooding while you arrange help. Know where your main shutoff is before a crisis — it is usually near the meter or where the line enters the house.</p>

          <h2>Freeze-related bursts in winter</h2>
          <p>Even in Rio Rancho’s generally mild winters, cold snaps can freeze pipes in garages, exterior walls, or uninsulated cavities. When ice melts, the cracked pipe releases water into framing and finishes. After a freeze warning, letting faucets drip slightly and opening cabinet doors under sinks on exterior walls are simple precautions many local homeowners use.</p>

          <h2>What providers often do after a pipe break</h2>
          <p>Restoration companies typically focus on the water damage side: extraction, moisture mapping, drying, and cleaning. A licensed plumber may be needed separately to repair or repipe the failed section. Ask who handles which part of the job so you are not surprised by the sequence of trades.</p>
          <p>For slab leaks, specialists may use electronic leak detection or other methods to locate the break before repairs. Once the plumbing is addressed, drying the surrounding structure remains important so moisture does not linger under flooring.</p>

          <h2>Water heaters and appliance lines</h2>
          <p>Tank water heaters can leak at fittings or fail at the tank itself. Washing machine hoses and refrigerator ice-maker lines are frequent culprits in laundry rooms and kitchens. If an appliance is involved, unplug it only if you can do so without stepping in water near outlets.</p>

          <h2>Get a referral for leak-related damage</h2>
          <p>Call <a class="phone-link" href="tel:{PHONE_TEL}">{PHONE_DISP}</a> to use our free referral service. We help connect Rio Rancho-area homeowners with independent water damage providers who can discuss drying and cleanup after a burst pipe or leak. Plumbing repairs are handled by appropriate licensed trades; we do not perform that work.</p>
          <p>Learn more about broader <a href="water-damage-restoration.html">restoration</a> and possible <a href="mold-remediation.html">mold follow-up</a> if moisture was present for a while.</p>
''',
    "Burst Pipe and Leak Water Damage Referral",
    "Free referral for burst pipe and leak water damage help near Rio Rancho, NM.",
)

service_page(
    "mold-remediation.html",
    "mold",
    "Mold Remediation Referral | Rio Rancho, NM",
    "Concerned about mold after a leak or flood in Rio Rancho? Call our free referral line to connect with independent mold remediation providers.",
    "Mold Remediation After Water Damage",
    "Mold often follows unresolved moisture. If you have musty odors, visible growth, or a recent leak, we can help connect you with independent mold remediation providers.",
    f'''          <p>Mold needs moisture and a food source — drywall paper, dust, wood, and many household materials can qualify. In a dry region like central New Mexico, outdoor humidity is often low, but indoor leaks, poor drying after a flood, and cooler condensation issues still create mold problems inside homes. Our referral service focuses on connecting callers who need mold remediation help, especially when it is tied to water damage.</p>

          <h2>When mold concerns usually show up</h2>
          <p>Homeowners often call after noticing a persistent musty smell, spotting discoloration on walls or ceilings, or finding growth behind a recently wet baseboard. Others are dealing with a known leak that sat for days or weeks. Not every stain is mold, and not every musty smell means the same scope of work — a proper assessment matters before tear-out begins.</p>

          <h2>What mold remediation generally involves</h2>
          <p>Independent mold remediation providers typically identify and address the moisture source first (or coordinate with whoever is fixing it), isolate work areas when appropriate, remove or clean affected materials, and dry the space. Porous materials that are heavily colonized are often discarded rather than cleaned. The right approach depends on the size of the area, the materials involved, and occupant sensitivity.</p>
          <ul>
            <li>Confirm moisture is stopped or controlled</li>
            <li>Assess visible growth and hidden cavities when needed</li>
            <li>Contain dust during removal when the job calls for it</li>
            <li>Clean and treat surfaces per the provider’s methods</li>
            <li>Verify the area is dry before closing walls back up</li>
          </ul>

          <h2>Water damage and mold are linked</h2>
          <p>If you still have active leaking, fixing mold symptoms alone will not solve the problem. Likewise, if flood water was removed but materials never fully dried, mold can appear later. That is why many callers need both water damage drying support and mold remediation guidance. You can start with either our <a href="water-damage-restoration.html">water damage</a> or mold page — describe what you are seeing when you call.</p>

          <h2>What we will not claim</h2>
          <p>We do not diagnose health conditions, guarantee “mold-free” homes, or promise laboratory results. We also do not pretend to be a remediation contractor. If you have medical concerns, speak with a qualified health professional. For the home itself, ask the provider about their process, licensing where applicable, and how they will handle your specific rooms.</p>

          <h2>Prevention tips after a leak</h2>
          <ol>
            <li>Dry wet materials as promptly as safety allows.</li>
            <li>Run ventilation in bathrooms and kitchens.</li>
            <li>Watch evaporative cooler drains and pads for overflow.</li>
            <li>Fix plumbing drips instead of placing a bucket long-term.</li>
            <li>After storms, check ceilings and closets for new stains.</li>
          </ol>

          <h2>Request a mold remediation referral</h2>
          <p>Call <a class="phone-link" href="tel:{PHONE_TEL}">{PHONE_DISP}</a>. There is no fee to use this referral line. We help connect you with an independent provider serving Rio Rancho and nearby communities. Hiring decisions remain yours.</p>
''',
    "Mold Remediation Referral",
    "Free referral connecting callers with independent mold remediation providers near Rio Rancho, NM.",
)

# Service areas
pages["service-areas.html"] = (
    head(
        "Service Areas | Rio Rancho Water Damage Referral",
        "We connect homeowners in Rio Rancho, Corrales, Bernalillo, Placitas, and Northwest Albuquerque with independent water damage providers.",
        "service-areas.html",
    )
    + header("areas")
    + f'''  <main>
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumb"><a href="index.html">Home</a> / Service Areas</p>
        <h1>Service Areas</h1>
        <p class="lead">Our free referral line focuses on Rio Rancho and nearby communities in Sandoval County and Northwest Albuquerque. Provider availability can vary by day and by exact location.</p>
      </div>
    </section>
    <section class="section">
      <div class="container content-split">
        <article class="prose">
          <p>When you call, tell us your city or neighborhood. We use that information to connect you with an independent water damage or mold remediation provider who serves your area when one is available.</p>

          <h2>Primary focus: Rio Rancho</h2>
          <p>Rio Rancho is our main coverage city. That includes established areas as well as growing neighborhoods across the city. Whether you are dealing with a monsoon leak in Enchanted Hills, a water heater failure near Northern Meadows, or a cooler overflow in Cabezon, you can call the same referral number.</p>

          <h2>Nearby communities</h2>
          <ul class="area-list">
            <li>Rio Rancho</li>
            <li>Corrales</li>
            <li>Bernalillo</li>
            <li>Placitas</li>
            <li>Northwest Albuquerque</li>
            <li>Paradise Hills area</li>
            <li>Taylor Ranch area</li>
            <li>Los Ranchos (nearby)</li>
          </ul>

          <h2>Neighborhoods often mentioned by callers</h2>
          <p>Callers commonly reference parts of Rio Rancho such as Enchanted Hills, Cabezon, Northern Meadows, Loma Colorado, Riverview, and areas along Unser Boulevard and NM 528. You do not need a perfect neighborhood name — a cross street or ZIP is enough when you call.</p>

          <h2>What “service area” means for a referral site</h2>
          <p>We are not a contractor with a fixed truck radius. We operate a phone referral connection. That means the independent provider you speak with sets their own travel area, schedule, and fees. If a provider cannot take your job, you can ask about alternatives when you call.</p>

          <h2>Outside these areas?</h2>
          <p>If you are elsewhere in the Albuquerque metro or broader New Mexico, you are still welcome to call. We will be honest if we cannot help with a connection for your location.</p>

          <div class="notice">
            <strong>Note:</strong> Listing a community here does not guarantee a provider is available at the moment you call. Availability depends on network coverage and the independent companies participating at that time.
          </div>
        </article>
        <aside>
          <div class="sidebar-card">
            <h2>Call for your area</h2>
            <p>Rio Rancho &amp; nearby</p>
            <div class="phone-display"><a class="phone-link" href="tel:{PHONE_TEL}">{PHONE_DISP}</a></div>
            <a class="btn btn-primary btn-block" href="tel:{PHONE_TEL}">Call Now</a>
          </div>
        </aside>
      </div>
    </section>
  </main>
'''
    + footer()
)

# About
pages["about.html"] = (
    head(
        "About This Referral Service | Rio Rancho Water Damage",
        "Learn how this free Rio Rancho water damage referral site works and what we do — and do not — provide.",
        "about.html",
    )
    + header("about")
    + f'''  <main>
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumb"><a href="index.html">Home</a> / About</p>
        <h1>About This Referral Service</h1>
        <p class="lead">We built this site to help homeowners facing water damage or mold concerns find a clear next step: a phone conversation with an independent local provider.</p>
      </div>
    </section>
    <section class="section">
      <div class="container prose">
        <h2>Who we are</h2>
        <p>Rio Rancho Water Damage is a <strong>free referral / connection service</strong>. We are not a restoration contractor, mold remediator, plumber, or insurance agency. We do not send technicians, submit insurance claims on your behalf, or perform cleanup work.</p>
        <p>When you call <a class="phone-link" href="tel:{PHONE_TEL}">{PHONE_DISP}</a>, your call may be connected or forwarded to an independent, licensed service provider who works in or near your area. That provider is a separate business. Any agreement you make is between you and them.</p>

        <h2>Why a referral site?</h2>
        <p>Searching online during a water emergency is overwhelming. Many results mix national call centers, ads, and local companies without explaining who will actually show up. Our goal is simpler: give Rio Rancho-area homeowners a straightforward number to call when they need to talk with someone about water extraction, drying, flood cleanup, or mold related to moisture.</p>

        <h2>What we provide</h2>
        <ul>
          <li>Educational pages about common water damage and mold situations</li>
          <li>A phone number you can call for a referral connection</li>
          <li>Clear disclosure that we are not the contractor</li>
        </ul>

        <h2>What we do not provide</h2>
        <ul>
          <li>On-site restoration, construction, or mold removal</li>
          <li>Guarantees about response time, pricing, or insurance coverage</li>
          <li>Medical advice about mold exposure</li>
          <li>A physical retail storefront for walk-in visits</li>
        </ul>

        <h2>Honesty matters</h2>
        <p>We do not invent reviews, licenses, certifications, or years in business for this site. We do not use someone else’s business name or address. Providers you may speak with should be asked directly about their credentials, insurance, and experience.</p>

        <h2>Questions about the site?</h2>
        <p>For referral calls, use <a class="phone-link" href="tel:{PHONE_TEL}">{PHONE_DISP}</a>. For website or privacy questions, see our <a href="contact.html">Contact</a>, <a href="privacy.html">Privacy Policy</a>, and <a href="terms.html">Terms of Use</a> pages.</p>
      </div>
    </section>
  </main>
'''
    + footer()
)

# Contact — phone only, no form
pages["contact.html"] = (
    head(
        "Contact | Rio Rancho Water Damage Referral",
        "Call our free Rio Rancho water damage referral line. Phone contact only — no form required.",
        "contact.html",
    )
    + header("contact")
    + f'''  <main>
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumb"><a href="index.html">Home</a> / Contact</p>
        <h1>Contact</h1>
        <p class="lead">The fastest way to reach us is by phone. There is no contact form on this site.</p>
      </div>
    </section>
    <section class="section">
      <div class="container" style="max-width:640px">
        <div class="card" style="text-align:center;padding:2.5rem 1.5rem">
          <h2 class="mt-0">Free referral line</h2>
          <p>For water damage, flood cleanup, burst pipes / leaks, or mold concerns in the Rio Rancho area:</p>
          <p style="font-size:1.75rem;font-weight:800;margin:1rem 0">
            <a class="phone-link" href="tel:{PHONE_TEL}">{PHONE_DISP}</a>
          </p>
          <a class="btn btn-primary btn-lg" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a>
          <p class="muted" style="margin-top:1.5rem;margin-bottom:0">Tap the button on a mobile phone to dial automatically.</p>
        </div>
        <div class="notice" style="margin-top:1.5rem">
          <strong>Reminder:</strong> This is a referral connection service. Calls may be forwarded to an independent provider. We do not have a public walk-in office listed on this site.
        </div>
        <p style="margin-top:1.5rem">Before you call, it helps to know: your city/neighborhood, what caused the water (if you know), which rooms are affected, and whether the water is still flowing.</p>
      </div>
    </section>
  </main>
'''
    + footer()
)

# Privacy
pages["privacy.html"] = (
    head(
        "Privacy Policy | Rio Rancho Water Damage",
        "Privacy Policy for the Rio Rancho Water Damage referral website.",
        "privacy.html",
    )
    + header("")
    + f'''  <main>
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumb"><a href="index.html">Home</a> / Privacy Policy</p>
        <h1>Privacy Policy</h1>
        <p class="lead">Last updated: November 9, 2026</p>
      </div>
    </section>
    <section class="section">
      <div class="container prose legal">
        <p>This Privacy Policy describes how the Rio Rancho Water Damage website (“this site,” “we,” “us”) handles information when you visit rioranchowaterdamage.com or call the phone number published on this site.</p>

        <h2>1. Who we are</h2>
        <p>This site operates as a free referral service that may connect callers with independent service providers. We are not those providers. This policy covers the website and the referral phone experience we control — not the privacy practices of third-party contractors you may later hire.</p>

        <h2>2. Information we may collect</h2>
        <h3>Website browsing</h3>
        <p>Like most websites, our hosting provider may automatically receive standard technical data such as IP address, browser type, device type, referring URL, pages requested, and timestamps. We do not run third-party advertising or analytics trackers on this site as configured.</p>
        <h3>Phone calls</h3>
        <p>If you call the number on this site, your telephone number and call metadata (such as time and duration) may be processed by our telephony provider and, when a referral is made, shared as needed with an independent provider to complete the connection. Call recording may occur depending on the telephony or network tools in use; if recording applies, listen for any notice at the start of the call.</p>
        <h3>Information you volunteer</h3>
        <p>During a call you may share details about your property, the water or mold issue, and your location so a provider can evaluate whether they can help. Share only what you are comfortable providing.</p>

        <h2>3. How information is used</h2>
        <ul>
          <li>To operate and secure the website</li>
          <li>To connect you with an independent provider when you request help by phone</li>
          <li>To troubleshoot call quality or misuse of the phone line</li>
          <li>To comply with law when required</li>
        </ul>

        <h2>4. Sharing of information</h2>
        <p>We may share call-related information with telephony platforms, call-tracking tools, pay-per-call or referral networks, and independent service providers solely to facilitate a referral you initiated. We do not sell personal information as a standalone data product. Providers you speak with have their own privacy practices once you are connected.</p>

        <h2>5. Cookies and local storage</h2>
        <p>This static website does not require accounts and is not intentionally configured with advertising cookies. Your browser may still store basic cache data for performance.</p>

        <h2>6. Data retention</h2>
        <p>Technical logs and call records are retained only as long as needed for operations, billing reconciliation with networks, dispute resolution, and legal obligations, then deleted or anonymized according to our vendors’ practices.</p>

        <h2>7. Children’s privacy</h2>
        <p>This site is intended for adults making decisions about property damage. We do not knowingly collect information from children under 13.</p>

        <h2>8. Security</h2>
        <p>No method of transmission or storage is 100% secure. We use reputable hosting and telephony vendors and limit access to call-related tools to what is needed to run the referral service.</p>

        <h2>9. Your choices</h2>
        <p>You may choose not to call. If you call, you may end the conversation at any time. For requests related to call data held by a telephony vendor or network, contact us via the phone number on this site and we will point you to the appropriate channel when we can.</p>

        <h2>10. Changes</h2>
        <p>We may update this Privacy Policy by posting a new version on this page with a revised “Last updated” date.</p>

        <h2>11. Contact</h2>
        <p>Questions about this policy: call <a class="phone-link" href="tel:{PHONE_TEL}">{PHONE_DISP}</a> and state that your question is about privacy (not an emergency referral).</p>
      </div>
    </section>
  </main>
'''
    + footer()
)

# Terms
pages["terms.html"] = (
    head(
        "Terms of Use | Rio Rancho Water Damage",
        "Terms of Use for the Rio Rancho Water Damage referral website.",
        "terms.html",
    )
    + header("")
    + f'''  <main>
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumb"><a href="index.html">Home</a> / Terms of Use</p>
        <h1>Terms of Use</h1>
        <p class="lead">Last updated: November 9, 2026</p>
      </div>
    </section>
    <section class="section">
      <div class="container prose legal">
        <p>These Terms of Use (“Terms”) govern your access to rioranchowaterdamage.com and related phone referral services. By using the site or calling the published number, you agree to these Terms.</p>

        <h2>1. Nature of the service</h2>
        <p><strong>This site is a free referral / lead-connection service.</strong> We do not perform water damage restoration, flood cleanup, plumbing, mold remediation, construction, or insurance adjusting. Calls may be forwarded or connected to an independent, licensed service provider in your area. Those providers are not our employees or partners in a joint venture unless explicitly stated in a separate written agreement.</p>

        <h2>2. No professional advice</h2>
        <p>Content on this website is for general informational purposes only. It is not a substitute for inspection by a qualified professional, legal advice, insurance advice, or medical advice. Always confirm facts about your home with appropriate licensed trades and your insurer.</p>

        <h2>3. No guarantees</h2>
        <p>We do not guarantee that a provider will answer, be available in your exact neighborhood, offer a particular price, meet a response-time expectation, or be the right fit for your job. We do not guarantee insurance coverage outcomes. Any warranties or service commitments are solely those offered (if any) by the independent provider you hire.</p>

        <h2>4. Your responsibilities</h2>
        <ul>
          <li>Provide accurate location and situation information when requesting a referral</li>
          <li>Verify licensing, insurance, scope, and pricing with any provider before authorizing work</li>
          <li>Exercise your own judgment about safety (electrical hazards, contaminated water, structural risk)</li>
          <li>Do not use the phone line for harassment, fraud, or unlawful purposes</li>
        </ul>

        <h2>5. Third-party providers</h2>
        <p>If you hire a provider, your contract is with them. We are not a party to that contract and are not responsible for their workmanship, billing, conduct, or omissions. Disputes about services should be raised directly with that provider.</p>

        <h2>6. Intellectual property</h2>
        <p>Website text, design, and branding elements are owned by the site operator or used with permission. You may not copy substantial portions for commercial reuse without permission.</p>

        <h2>7. Limitation of liability</h2>
        <p>To the fullest extent permitted by law, the site operator is not liable for indirect, incidental, special, consequential, or punitive damages, or for any loss arising from your use of the website, reliance on its content, or interactions with third-party providers connected through the referral line. Our total liability for claims relating to the site or referral service shall not exceed one hundred U.S. dollars (USD $100).</p>

        <h2>8. Indemnity</h2>
        <p>You agree to indemnify and hold harmless the site operator from claims arising out of your misuse of the site, your breach of these Terms, or your agreements with third-party providers.</p>

        <h2>9. Changes and availability</h2>
        <p>We may modify the website, phone routing, or these Terms at any time. Continued use after changes means you accept the updated Terms. We may suspend the referral line for maintenance or operational reasons.</p>

        <h2>10. Governing law</h2>
        <p>These Terms are governed by the laws of the State of New Mexico, without regard to conflict-of-law rules. Venue for disputes shall be in the state or federal courts located in New Mexico, unless applicable law requires otherwise.</p>

        <h2>11. Contact</h2>
        <p>Questions about these Terms: call <a class="phone-link" href="tel:{PHONE_TEL}">{PHONE_DISP}</a> and indicate your call is about website terms.</p>
      </div>
    </section>
  </main>
'''
    + footer()
)

# Write all pages
for name, html in pages.items():
    (ROOT / name).write_text(html, encoding="utf-8")
    print(f"Wrote {name} ({len(html)} bytes)")

print("Done", len(pages), "pages")
