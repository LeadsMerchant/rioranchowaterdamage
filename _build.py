#!/usr/bin/env python3
"""Generate the static site pages for rioranchowaterdamage.com (v2: seven service pages).
Existing live URLs are kept: flood-cleanup.html and burst-pipe-leak.html are still full pages.
Run:  python3 _build.py   (then ./replace_phone.sh once the tracking number exists)"""
from pathlib import Path
from _sitekit import Site, PHONE_DISP, PHONE_TEL, CALL

ROOT = Path(__file__).resolve().parent

CONFIG = {
    "domain": "rioranchowaterdamage.com",
    "brand": "Rio Rancho Water Damage",
    "logo_sub": "Local referral connection",
    "city": "Rio Rancho",
    "state": "New Mexico",
    "geo_region": "US-NM",
    "topbar": "Free referral for Rio Rancho homeowners",
    "footer_blurb": "A free referral service that helps homeowners in Rio Rancho and nearby communities connect with independent, licensed water damage, mold, sewage, and fire restoration providers.",
    "schema_areas": ["Corrales", "Bernalillo", "Placitas", "Albuquerque"],
    "law_state": "New Mexico",
    "year": 2026,
    "services": [
        {"file": "water-damage-restoration.html", "name": "Water Damage Restoration", "nav": "Water Damage Restoration", "icon": "🌊"},
        {"file": "storm-roof-leak-damage.html", "name": "Monsoon, Hail &amp; Roof Leaks", "nav": "Monsoon, Hail &amp; Roof Leaks", "icon": "⛈️"},
        {"file": "flood-cleanup.html", "name": "Flood Cleanup", "nav": "Flood Cleanup", "icon": "🌧️"},
        {"file": "burst-pipe-leak.html", "name": "Burst, Frozen &amp; Slab Leaks", "nav": "Burst, Frozen &amp; Slab Leaks", "icon": "🔧"},
        {"file": "sewage-backup-cleanup.html", "name": "Sewage Backup Cleanup", "nav": "Sewage Backup Cleanup", "icon": "🚽"},
        {"file": "mold-remediation.html", "name": "Mold Remediation", "nav": "Mold Remediation", "icon": "🦠"},
        {"file": "fire-smoke-damage.html", "name": "Fire &amp; Smoke Damage", "nav": "Fire &amp; Smoke Damage", "icon": "🔥"},
    ],
}

site = Site(CONFIG, ROOT)

# ======================= HOME =======================
home_faqs = [
    ("Is this a water damage restoration company?",
     "No. This website is a free referral service. When you call, we help connect you with an independent, licensed provider who can discuss your water, mold, sewage, or fire and smoke damage."),
    ("Can I call at night or on a weekend?",
     "Yes, you can call any time. Many restoration companies offer emergency response outside business hours, and we will try to connect you with one. We cannot promise a provider is available at every hour."),
    ("What areas near Rio Rancho do you cover?",
     "We focus on Rio Rancho (ZIP codes 87124 and 87144) and nearby communities including Corrales, Bernalillo, Placitas, and Northwest Albuquerque. Availability depends on the providers in our network at the time you call."),
    ("What kinds of problems can I call about?",
     "Monsoon and hail roof leaks, flash flooding, burst or frozen pipes, slab leaks, water heater failures, evaporative cooler overflows, sewage backups, mold after water damage, and fire or smoke damage."),
    ("Will I be charged for calling?",
     "There is no charge to call this referral line. Any fees for inspection or restoration work are between you and the independent provider you choose to hire."),
    ("Should I call my insurance company first?",
     "If the damage may be covered, it is often wise to document the situation and contact your insurer. A restoration provider can also walk you through typical next steps for your type of loss."),
    ("What should I do while I wait for help?",
     "If it is safe, shut off the water source, avoid electrical hazards, move valuables out of wet areas, and photograph the damage. Do not enter standing water if you suspect electrical risk or sewage contamination."),
]

svc_cards = [
    ("🌊", "Water Damage Restoration", "Help after leaks, appliance failures, and indoor water: extraction, drying, and cleanup.", "water-damage-restoration.html"),
    ("⛈️", "Monsoon, Hail &amp; Roof Leaks", "Summer storms that crack roofs, overflow canales, or push water past windows.", "storm-roof-leak-damage.html"),
    ("🌧️", "Flood Cleanup", "Storm runoff, arroyo flooding, or indoor flooding that soaked floors and belongings.", "flood-cleanup.html"),
    ("🔧", "Burst, Frozen &amp; Slab Leaks", "Frozen pipes, slab leaks, and supply-line failures can soak a home fast.", "burst-pipe-leak.html"),
    ("🚽", "Sewage Backup Cleanup", "Toilet, tub, or floor drain backups need protective handling.", "sewage-backup-cleanup.html"),
    ("🦠", "Mold Remediation", "When moisture lingers, mold can follow, even in a dry climate.", "mold-remediation.html"),
    ("🔥", "Fire &amp; Smoke Damage", "Soot, smoke odor, and the water left behind by firefighting.", "fire-smoke-damage.html"),
]
cards_html = "\n".join(f'''          <article class="card">
            <div class="icon" aria-hidden="true">{i}</div>
            <h3>{t}</h3>
            <p>{d}</p>
            <a class="more" href="{h}">Learn more →</a>
          </article>''' for i, t, d, h in svc_cards)

home_schema_site = {
    "@context": "https://schema.org", "@type": "WebSite",
    "name": CONFIG["brand"], "url": site.url(),
    "description": "Free referral service connecting Rio Rancho, NM homeowners with independent water damage, mold, sewage, and fire restoration providers.",
}
home_schema_org = {
    "@context": "https://schema.org",
    **site.org(),
    "areaServed": site.area_served(),
    "knowsAbout": ["Water damage restoration", "Monsoon and roof leak water damage", "Flood cleanup",
                   "Burst pipe and slab leak water damage", "Sewage backup cleanup", "Mold remediation",
                   "Fire and smoke damage restoration"],
    "hasOfferCatalog": {
        "@type": "OfferCatalog", "name": "Referral services",
        "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"].replace("&amp;", "&"), "url": site.url(s["file"])}} for s in CONFIG["services"]],
    },
}

home = (site.head("Rio Rancho Water Damage Help | Free Local Referral",
                  "Water damage, monsoon leaks, burst pipes, sewage, mold, or fire damage in Rio Rancho, NM? Call free to reach independent local restoration providers.",
                  "", [home_schema_site, home_schema_org, site.faq_schema(home_faqs)])
        + site.header("index.html")
        + f'''  <main>
    <section class="hero">
      <div class="container hero-grid">
        <div>
          <div class="hero-badge">Rio Rancho · Corrales · Bernalillo · NW Albuquerque</div>
          <h1>Water damage in Rio Rancho? Get connected to local help.</h1>
          <p class="lead">We are a free referral service for homeowners dealing with monsoon leaks, flooding, burst pipes, sewage backups, mold, and fire or smoke damage. Call and we will help connect you with an independent, licensed provider in your area.</p>
          <div class="hero-actions">
            <a class="btn btn-primary btn-lg" href="tel:{PHONE_TEL}">📞 Call {PHONE_DISP}</a>
            <a class="btn btn-secondary btn-lg" href="#services">See what we cover</a>
          </div>
          <p class="hero-note">No charge to call, day or night. Which providers can respond depends on the hour and your location. We do not perform restoration work ourselves.</p>
        </div>
        <aside class="hero-card" aria-label="Common reasons to call">
          <h2>Common reasons homeowners call</h2>
          <ul>
            <li>Monsoon storm water came through the roof or under a door</li>
            <li>Burst pipe, slab leak, or water heater failure</li>
            <li>Swamp cooler overflow dripping through the ceiling</li>
            <li>Toilet, tub, or floor drain backing up sewage</li>
            <li>Musty smell or visible mold after a leak</li>
            <li>Soot, smoke odor, or water after a fire</li>
          </ul>
        </aside>
      </div>
    </section>

    <section class="emergency-band" aria-label="Emergency help">
      <div class="container emergency-inner">
        <div>
          <h2>Water coming in right now? Call any time, day or night.</h2>
          <p>If it is safe, shut off the main water valve and stay away from wet outlets. Then call. Many restoration companies run 24/7 emergency crews, and we will try to connect you with one that serves your address.</p>
        </div>
        <a class="btn btn-primary btn-lg" href="tel:{PHONE_TEL}">🚨 Emergency: {PHONE_DISP}</a>
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
            <p>Tell us what happened: a storm leak, a burst pipe, a sewage backup, mold, or a fire. Share your location in or near Rio Rancho.</p>
          </div>
          <div class="step">
            <h3>Get connected</h3>
            <p>We help connect you with an independent provider who handles that type of damage in the area.</p>
          </div>
          <div class="step">
            <h3>Talk through next steps</h3>
            <p>Ask about inspection, drying, cleanup, and documentation. Hiring decisions and pricing are always between you and the provider.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt" id="services">
      <div class="container">
        <div class="section-head">
          <h2>Services we can refer you for</h2>
          <p>One number for water, sewage, mold, and fire damage in Rio Rancho-area homes.</p>
        </div>
        <div class="card-grid card-grid-3">
{cards_html}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2>Why Rio Rancho homes deal with water damage</h2>
          <p>Local conditions create real moisture risks, even in a dry climate.</p>
        </div>
        <div class="card-grid card-grid-3">
          <div class="card">
            <h3>Monsoon season</h3>
            <p>The National Weather Service in Albuquerque defines monsoon season as June 15 through September 30, with flash flooding, damaging winds, and hail among its hazards. Short, intense storms overwhelm roofs and drainage.</p>
          </div>
          <div class="card">
            <h3>Arroyos and runoff</h3>
            <p>The Southern Sandoval County Arroyo Flood Control Authority (SSCAFCA) manages flood and erosion risk along the arroyos that cross Rio Rancho. Its hazard plan lists repeated flood events in the city.</p>
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
            <h3>Slab leaks and water heaters</h3>
            <p>Pipes under concrete slabs can leak out of sight, and aging water heaters can fail without much warning.</p>
          </div>
          <div class="card">
            <h3>Wildfire smoke</h3>
            <p>New Mexico’s largest fires, like the 2011 Las Conchas Fire in the Jemez Mountains, show how much smoke the region can see. Smoke and soot inside a home need cleanup too.</p>
          </div>
        </div>
        <p class="source-note">Sources: NWS Albuquerque Monsoon Awareness; SSCAFCA 2026 Hazard Mitigation Plan public review draft; National Park Service (Las Conchas Fire).</p>
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
{site.faq_html(home_faqs)}
        </div>
      </div>
    </section>

    <section class="cta-band">
      <div class="container">
        <h2>Ready to talk with someone about your damage?</h2>
        <p>Call our free Rio Rancho referral line. We will help connect you with an independent local provider.</p>
        <a class="btn btn-primary btn-lg" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a>
      </div>
    </section>
  </main>
'''
        + site.footer())
site.raw_page("index.html", home, "monthly", "1.0")

# ======================= SERVICE PAGES =======================
site.service_page({
    "file": "water-damage-restoration.html",
    "title": "Water Damage Restoration Referral | Rio Rancho, NM",
    "meta": "Get connected with independent water damage restoration providers serving Rio Rancho, Corrales, Bernalillo, and NW Albuquerque.",
    "crumb": "Water Damage Restoration",
    "h1": "Water Damage Restoration in Rio Rancho",
    "lead": "When water gets into your home, acting quickly can limit damage to floors, walls, and belongings. Our free referral line helps Rio Rancho-area homeowners connect with independent restoration providers.",
    "schema_name": "Water Damage Restoration Referral",
    "service_type": "Water damage restoration",
    "schema_desc": "Free referral connecting Rio Rancho homeowners with independent water damage restoration providers.",
    "prio": "0.9",
    "body": '''          <p>Water damage is stressful whether it started with a sudden pipe break or a slow drip you only noticed after floors felt soft. In Rio Rancho and nearby communities, homeowners also deal with monsoon-driven roof and window leaks, evaporative cooler overflows, and winter freezes that crack pipes. This page explains what restoration typically involves and how our referral service can help you reach someone who does the work.</p>

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
          <p>New Mexico’s climate is dry overall, but that does not protect homes from indoor plumbing failures or intense summer storms. Local triggers include monsoon downpours that overwhelm roof drains and canales (see <a href="storm-roof-leak-damage.html">monsoon, hail, and roof leaks</a>), frozen pipes during cold snaps, swamp cooler drain problems, failed water heaters, supply-line breaks under sinks, and slab leaks that go unnoticed until flooring cups or water bills jump (see <a href="burst-pipe-leak.html">burst, frozen, and slab leaks</a>).</p>
          <p>Whether you live in Enchanted Hills, Cabezon, Northern Meadows, or closer to Corrales and Bernalillo, the same advice applies: stop the water if you safely can, document what you see, and get a professional assessment before materials sit wet for days.</p>

          <h2>Why drying matters as much as cleanup</h2>
          <p>Removing visible water is only part of the job. Dry desert air makes carpet and paint feel normal quickly, but moisture trapped in carpet pad, baseboards, drywall, and subfloors can keep feeding damage, including odors and <a href="mold-remediation.html">mold</a>, after the surface looks dry. Providers use moisture meters, air movers, and dehumidifiers to bring materials back to a safer moisture level. Asking how they will verify dryness is a reasonable question before you authorize work.</p>

          <h2>Clean water vs. contaminated water</h2>
          <p>A supply line break usually starts clean. Water that came up through a toilet, tub, or floor drain is treated as contaminated and needs a different process; see <a href="sewage-backup-cleanup.html">sewage backup cleanup</a>. Tell the provider where the water came from so they can plan correctly.</p>

          <h2>Practical steps you can take right away</h2>
          <ol>
            <li>If it is safe, shut off the water supply to the leak or the whole house.</li>
            <li>Avoid standing water near electrical outlets, panels, or appliances.</li>
            <li>Move furniture and valuables out of wet zones when you can do so safely.</li>
            <li>Take clear photos and short videos of affected rooms.</li>
            <li>Note the time the problem started and any recent weather or plumbing work.</li>
            <li>Call {CALL} for a free referral to a restoration provider.</li>
          </ol>
''',
    "faqs": [
        ("How fast should drying start?",
         "As soon as possible. Many providers aim to start extraction and drying the same day, because materials that stay wet longer are more likely to need replacement."),
        ("Do you fix the leak too?",
         "No. Restoration companies handle the water damage. A licensed plumber usually repairs the pipe or appliance connection. Ask who handles each part of the job."),
    ],
})

site.service_page({
    "file": "storm-roof-leak-damage.html",
    "title": "Monsoon, Hail & Roof Leak Water Damage | Rio Rancho, NM",
    "meta": "Monsoon storm, hail, or a roof leak let water into your Rio Rancho home? Call free to connect with independent storm water damage providers.",
    "crumb": "Monsoon, Hail &amp; Roof Leaks",
    "h1": "Monsoon, Hail &amp; Roof Leak Water Damage",
    "lead": "Rio Rancho can go weeks without rain, then get a downpour in twenty minutes. When a monsoon storm finds a weak spot in the roof or a clogged canale, we can connect you with an independent provider who dries out what got wet.",
    "schema_name": "Monsoon and Roof Leak Water Damage Referral",
    "service_type": "Storm and roof leak water damage restoration",
    "schema_desc": "Free referral for monsoon, hail, and roof leak water damage help in Rio Rancho, New Mexico.",
    "side_h": "Ceiling leaking?",
    "side_p": "Catch the drip, keep clear of light fixtures, then call.",
    "body": '''          <p>The National Weather Service in Albuquerque defines New Mexico’s monsoon season as June 15 through September 30. It lists flash flooding, damaging winds, hail, and lightning among the hazards. Storms often build over the mountains in the afternoon and move into lower areas, which means a dry morning in Rio Rancho can turn into a roof leak by evening.</p>

          <h2>How storm water gets in on New Mexico homes</h2>
          <ul>
            <li><strong>Flat and low-slope roofs.</strong> Many Southwest-style homes have flat roofs with parapet walls. Water pools if roof drains or canales are clogged, then finds cracks in the roofing.</li>
            <li><strong>Canales and scuppers</strong> blocked by leaves, tumbleweeds, or debris, so water backs up behind the parapet.</li>
            <li><strong>Hail</strong> cracking shingles, tiles, skylights, or cooler housings.</li>
            <li><strong>Sun-worn roofing.</strong> Intense sun and big temperature swings age roof coatings and sealants.</li>
            <li><strong>Stucco cracks and window seals</strong> letting wind-driven rain into walls.</li>
            <li><strong>Evaporative coolers</strong> on the roof whose curbs or ducts leak during heavy rain.</li>
          </ul>

          <h2>Signs of a roof leak</h2>
          <p>Brown rings or bubbling paint on the ceiling, a sagging drywall spot, water dripping from a light fixture or vent, damp attic insulation, or staining near the top of an exterior wall after a storm.</p>

          <h2>Two jobs: the roof and the inside</h2>
          <p>A roofer stops the water from getting in. A restoration provider handles what already got in: wet insulation, ceiling drywall, framing, and floors below. Many homeowners need both. Ask who will tarp or temporarily seal the roof, and how quickly.</p>

          <h2>During and after a storm</h2>
          <ol>
            <li>Put a bucket under drips. Keep people out from under any ceiling that is bulging with water.</li>
            <li>Turn off power to leaking light fixtures and fans.</li>
            <li>When it is safe, check canales and roof drains for clogs.</li>
            <li>Photograph the ceiling, attic, and outside of the home for your records.</li>
            <li>Be careful with door-to-door contractors after hail; verify any company before signing.</li>
            <li>Call {CALL} to be connected with a provider for the interior water damage.</li>
          </ol>
          <p>If storm water came in at ground level instead, see <a href="flood-cleanup.html">flood cleanup</a>. If ceiling or attic materials stayed wet, see <a href="mold-remediation.html">mold remediation</a>.</p>
          <p class="source-note">Source: National Weather Service Albuquerque, Monsoon Awareness pages.</p>
''',
    "faqs": [
        ("Do you repair roofs?",
         "No. We are a referral service focused on the water damage inside your home. You will need a roofer for the roof itself."),
        ("Can a small ceiling stain wait until after monsoon season?",
         "A stain means water reached the drywall. It is worth having the roof and attic checked before the next storm adds more water."),
    ],
})

site.service_page({
    "file": "flood-cleanup.html",
    "title": "Flood Cleanup Referral | Rio Rancho, NM",
    "meta": "Flooding from storms, arroyo runoff, or indoor failures? Call our free Rio Rancho referral line to connect with independent flood cleanup providers.",
    "crumb": "Flood Cleanup",
    "h1": "Flood Cleanup Help for Rio Rancho Homes",
    "lead": "Storm water, monsoon runoff, or indoor flooding can soak a home in minutes. We help you connect with independent providers who handle flood cleanup and drying.",
    "schema_name": "Flood Cleanup Referral",
    "service_type": "Flood cleanup and water extraction",
    "schema_desc": "Free referral for flood cleanup assistance in Rio Rancho, New Mexico.",
    "body": '''          <p>Flooding does not only mean a river overflowing. For many Rio Rancho homeowners, “flood cleanup” means several inches of water across a garage, living room, or hallway after a fierce monsoon cell, a blocked drain, or a major indoor plumbing failure. Basements are less common here than in many parts of the country, so water usually spreads across main floors, garages, and slab-level rooms. Fast removal of water and a careful drying plan protect flooring, cabinets, and wall cavities from longer-term damage.</p>

          <h2>Arroyos, runoff, and flash floods</h2>
          <p>Rio Rancho is crossed by arroyos that carry storm water toward the Rio Grande. The Southern Sandoval County Arroyo Flood Control Authority (SSCAFCA), which serves Rio Rancho, Corrales, and Bernalillo, manages flood and erosion risk along them. Its 2026 hazard mitigation plan draft lists more than a dozen flood events affecting Rio Rancho since 2006, drawn from NOAA records. SSCAFCA also publishes an interactive map with “lateral erosion envelopes,” the areas near arroyos at higher risk, and FEMA flood maps show mapped floodplains.</p>
          <p>Homes on lower lots, near arroyos, or with below-grade entries can be more exposed when drainage is blocked by debris. Clearing gutters and canales and keeping downspouts directed away from the foundation are useful prevention steps after you stabilize the current problem.</p>

          <h2>Outdoor storms vs. indoor flooding</h2>
          <p>Water that entered from outside, through a door threshold, garage, or yard drainage problem, may carry soil and debris. Water from a clean supply line break is different from water that backed up from a drain or sewer (see <a href="sewage-backup-cleanup.html">sewage backup cleanup</a>). Providers categorize water by how contaminated it may be, because that affects cleaning methods and what materials can be kept.</p>

          <h2>What flood cleanup typically involves</h2>
          <ul>
            <li>Water extraction from floors and low spots</li>
            <li>Mud and debris removal when outside water came in</li>
            <li>Assessment of carpet, pad, baseboards, and drywall</li>
            <li>Cleaning and sanitizing appropriate surfaces</li>
            <li>Structural drying with monitored equipment</li>
            <li>Guidance on what to discard vs. attempt to restore</li>
          </ul>

          <h2>Safety first</h2>
          <p>Never drive or walk through moving water in an arroyo or flooded street; the National Weather Service warns that flash floods can rise with little notice. Inside, do not walk through floodwater if you suspect live electricity, and stay out of areas with sewage contamination unless you have proper protection.</p>

          <h2>Insurance note</h2>
          <p>Standard homeowners policies typically do not cover flooding from outside surface water; that usually requires separate flood insurance. Water from a burst pipe is often handled differently. Check your own policy.</p>

          <h2>Call for a flood cleanup referral</h2>
          <p>Our line at {CALL} is a free way to request a connection to an independent flood cleanup provider serving Rio Rancho and nearby towns. We are not the cleanup company. You decide whether to schedule service after you speak with them.</p>
          <p class="source-note">Sources: SSCAFCA (about, maps, 2026 HMP public review draft); NWS Albuquerque flash flood awareness.</p>
''',
    "faqs": [
        ("Is flood water from a storm treated differently than a pipe leak?",
         "Usually, yes. Outside water can carry soil and contaminants, so providers may remove more porous materials and sanitize surfaces."),
        ("How can I find out if my home is near a flood hazard?",
         "SSCAFCA publishes an interactive map of arroyo erosion hazard areas, and FEMA’s Flood Map Service Center shows mapped floodplains."),
    ],
})

site.service_page({
    "file": "burst-pipe-leak.html",
    "title": "Burst Pipe, Frozen Pipe & Slab Leak Damage | Rio Rancho",
    "meta": "Burst or frozen pipe, slab leak, or supply line failure in Rio Rancho? Call for a free referral to independent water damage providers.",
    "crumb": "Burst, Frozen &amp; Slab Leaks",
    "h1": "Burst Pipe, Frozen Pipe &amp; Slab Leak Water Damage",
    "lead": "A broken pipe can release a surprising amount of water in a short time. Get connected with independent providers who assess and dry leak-related damage in the Rio Rancho area.",
    "schema_name": "Burst Pipe, Frozen Pipe and Slab Leak Water Damage Referral",
    "service_type": "Burst pipe and slab leak water damage restoration",
    "schema_desc": "Free referral for burst pipe, frozen pipe, and slab leak water damage help near Rio Rancho, NM.",
    "side_h": "Pipe just burst?",
    "side_p": "Shut off the main water valve first, then call.",
    "body": '''          <p>Burst pipes and hidden leaks are among the most common indoor water emergencies. Supply lines under sinks, toilet connectors, water heaters, washing machine hoses, and pipes in attics, garages, or exterior walls can fail from age, freezing, corrosion, or accidental damage during renovations. In slab-on-grade homes, common across New Mexico, leaks under the concrete can be harder to spot until damage spreads.</p>

          <h2>Signs you may have an active leak</h2>
          <ul>
            <li>A drop in water pressure or the sound of running water when fixtures are off</li>
            <li>Warm spots on floors (sometimes a sign of a hot-water slab leak)</li>
            <li>An unexplained jump in the water bill</li>
            <li>Soft, stained, or cupping flooring</li>
            <li>Peeling paint, bubbling drywall, or damp baseboards</li>
            <li>Musty odor in a closet, cabinet, or closed room</li>
          </ul>
          <p>If you can find the shutoff valve, turning off the water can prevent more flooding while you arrange help. Know where your main shutoff is before a crisis; it is usually near the meter or where the line enters the house.</p>

          <h2>Freeze-related bursts in winter</h2>
          <p>Rio Rancho winters are generally mild by day, but nights regularly drop below freezing, and cold snaps can freeze pipes in garages, exterior walls, attics, and uninsulated cavities. The leak often starts when the ice melts and the cracked pipe releases water into framing and finishes. Common trouble spots include outdoor faucets with hoses still attached, drip irrigation and backflow devices, and lines feeding a rooftop swamp cooler that was not drained for winter.</p>
          <p>After a freeze warning, letting faucets drip, opening cabinet doors under sinks on exterior walls, and disconnecting hoses are simple precautions.</p>

          <h2>What providers often do after a pipe break</h2>
          <p>Restoration companies typically focus on the water damage side: extraction, moisture mapping, drying, and cleaning. A licensed plumber may be needed separately to repair or repipe the failed section. Ask who handles which part of the job so you are not surprised by the order of trades.</p>
          <p>For slab leaks, specialists may use electronic leak detection or other methods to locate the break before repairs. Once the plumbing is fixed, drying the surrounding structure still matters so moisture does not linger under flooring.</p>

          <h2>Water heaters and appliance lines</h2>
          <p>Tank water heaters can leak at fittings or fail at the tank itself. Washing machine hoses and refrigerator ice-maker lines are frequent culprits in laundry rooms and kitchens. If an appliance is involved, unplug it only if you can do so without stepping in water near outlets.</p>

          <h2>Get a referral for leak-related damage</h2>
          <p>Call {CALL} to use our free referral service. We help connect Rio Rancho-area homeowners with independent water damage providers who can discuss drying and cleanup after a burst pipe or leak. Plumbing repairs are handled by licensed plumbers; we do not perform that work.</p>
          <p>See also <a href="water-damage-restoration.html">water damage restoration</a> and <a href="mold-remediation.html">mold follow-up</a> if moisture was present for a while.</p>
''',
    "faqs": [
        ("Is a slab leak an emergency?",
         "An active leak under the slab keeps adding water under your floors. Shut off the main if you can, and have it located and repaired promptly so drying can start."),
        ("Is a burst pipe covered by insurance?",
         "Policies vary. Sudden bursts are often treated differently than slow leaks. Check your policy and talk to your insurer."),
    ],
})

site.service_page({
    "file": "sewage-backup-cleanup.html",
    "title": "Sewage Backup Cleanup Referral | Rio Rancho, NM",
    "meta": "Sewage backing up through a toilet, tub, or floor drain in Rio Rancho? Call free to connect with independent sewage cleanup and sanitizing providers.",
    "crumb": "Sewage Backup Cleanup",
    "h1": "Sewage Backup Cleanup in Rio Rancho",
    "lead": "Sewage is the one kind of water damage you should not clean up yourself. We connect Rio Rancho homeowners with independent providers equipped to remove contaminated water and sanitize the area.",
    "schema_name": "Sewage Backup Cleanup Referral",
    "service_type": "Sewage backup cleanup and sanitization",
    "schema_desc": "Free referral for sewage backup cleanup in Rio Rancho, New Mexico.",
    "side_h": "Sewage on the floor?",
    "side_p": "Stop using water, keep kids and pets away, and call.",
    "body": '''          <p>In a slab-on-grade home, a sewage backup usually shows up at the lowest fixture: a ground-floor toilet, tub, shower, or laundry drain. It can be a slow seep or a sudden overflow. Either way, the water carries bacteria and other contaminants, and porous materials it touched, like carpet, pad, drywall, and insulation, are usually removed rather than cleaned.</p>

          <h2>Common causes</h2>
          <ul>
            <li>Grease, wipes (even “flushable” ones), and other debris clogging the line</li>
            <li>Tree or shrub roots growing into the sewer lateral</li>
            <li>A cracked, sagging, or broken section of line</li>
            <li>A blockage in the city main</li>
            <li>A full or failing septic system on properties not served by city sewer</li>
          </ul>

          <h2>Who is responsible for the line?</h2>
          <p>Under Rio Rancho’s water and wastewater rules, the homeowner maintains the sewer lateral from the house to the public sewer, and the city’s utility is responsible for the sewer main lines, including stoppages in the main that cause backups. The city’s FAQ says to call the City right away if sewage is backing up into your house, and to call a plumber if the City is closed. You can find the current utility numbers on rrnm.gov.</p>

          <h2>What to do right now</h2>
          <ol>
            <li>Stop running water: no flushing, laundry, dishwasher, or showers until the line is cleared.</li>
            <li>Keep children, pets, and anyone with health concerns away.</li>
            <li>Do not touch the water without gloves and boots, and wash well afterward.</li>
            <li>Turn off power to the area if you can do it without stepping in water.</li>
            <li>Report a possible main-line problem to the City, or call a plumber to clear your line.</li>
            <li>Call {CALL} for a referral to a cleanup provider.</li>
          </ol>

          <h2>What professional sewage cleanup involves</h2>
          <p>Providers typically wear protective gear, extract the contaminated water, remove affected porous materials, clean and disinfect hard surfaces, and dry the area. Some also use air scrubbers for odor. Because the water is contaminated, more material usually has to go than with a clean-water leak.</p>

          <h2>Prevent the next one</h2>
          <ul>
            <li>Keep grease and wipes out of drains.</li>
            <li>Have older lines scoped with a camera if you have repeated slow drains or gurgling.</li>
            <li>Ask a plumber whether a backwater valve makes sense for your home.</li>
            <li>Check your insurance for a sewer or drain backup endorsement; many basic policies exclude it.</li>
          </ul>
          <p>Related: <a href="flood-cleanup.html">flood cleanup</a> and <a href="mold-remediation.html">mold remediation</a>.</p>
          <p class="source-note">Sources: Rio Rancho Code of Ordinances, Chapter 51 (water and wastewater rules); City of Rio Rancho Utilities FAQ.</p>
''',
    "faqs": [
        ("Can I clean up a small sewage backup myself?",
         "A very small amount on a hard, non-porous floor is sometimes handled by homeowners with gloves and disinfectant. Anything on carpet, drywall, or larger areas should be handled by a professional."),
        ("Will the smell go away on its own?",
         "Not usually, if contaminated materials are left in place. Removing affected materials and drying the area is what removes the source of the odor."),
    ],
})

site.service_page({
    "file": "mold-remediation.html",
    "title": "Mold Remediation Referral | Rio Rancho, NM",
    "meta": "Concerned about mold after a leak or flood in Rio Rancho? Call our free referral line to connect with independent mold remediation providers.",
    "crumb": "Mold Remediation",
    "h1": "Mold Remediation After Water Damage",
    "lead": "Mold often follows unresolved moisture. If you have musty odors, visible growth, or a recent leak, we can help connect you with independent mold remediation providers.",
    "schema_name": "Mold Remediation Referral",
    "service_type": "Mold remediation",
    "schema_desc": "Free referral connecting callers with independent mold remediation providers near Rio Rancho, NM.",
    "body": '''          <p>Mold needs moisture and a food source, and drywall paper, dust, wood, and many household materials qualify. In a dry region like central New Mexico, outdoor humidity is often low, but indoor leaks, poor drying after a flood, and evaporative cooler problems still create mold inside homes. Our referral service connects callers who need mold remediation help, especially when it is tied to water damage.</p>

          <h2>When mold concerns usually show up</h2>
          <p>Homeowners often call after noticing a persistent musty smell, spotting discoloration on walls or ceilings, or finding growth behind a recently wet baseboard. Others are dealing with a known leak that sat for days or weeks. Not every stain is mold, and not every musty smell means the same scope of work, so a proper assessment matters before tear-out begins.</p>

          <h2>Local moisture sources to check</h2>
          <ul>
            <li>Swamp cooler overflows, leaky ducts, or wet pads dripping into the attic</li>
            <li>Ceilings and attics after a <a href="storm-roof-leak-damage.html">monsoon roof leak</a></li>
            <li>Flooring and baseboards after a <a href="burst-pipe-leak.html">slab leak or burst pipe</a></li>
            <li>Walls and floors that were not fully dried after <a href="flood-cleanup.html">flooding</a></li>
            <li>Bathrooms without a working exhaust fan</li>
          </ul>

          <h2>What mold remediation generally involves</h2>
          <p>Independent mold remediation providers typically address the moisture source first (or coordinate with whoever is fixing it), isolate work areas when appropriate, remove or clean affected materials, and dry the space. Heavily affected porous materials are often thrown out rather than cleaned. The right approach depends on the size of the area, the materials involved, and how sensitive the people living there are.</p>
          <ul>
            <li>Confirm moisture is stopped or controlled</li>
            <li>Assess visible growth and hidden cavities when needed</li>
            <li>Contain dust during removal when the job calls for it</li>
            <li>Clean and treat surfaces using the provider’s methods</li>
            <li>Verify the area is dry before closing walls back up</li>
          </ul>

          <h2>What we will not claim</h2>
          <p>We do not diagnose health conditions, guarantee “mold-free” homes, or promise laboratory results. We also do not pretend to be a remediation contractor. If you have medical concerns, speak with a qualified health professional. For the home itself, ask the provider about their process, training (for example, IICRC), and how they will handle your specific rooms.</p>

          <h2>Prevention tips after a leak</h2>
          <ol>
            <li>Dry wet materials as promptly as safety allows.</li>
            <li>Run ventilation in bathrooms and kitchens.</li>
            <li>Watch evaporative cooler drains and pads for overflow, and drain the cooler for winter.</li>
            <li>Fix plumbing drips instead of leaving a bucket under them.</li>
            <li>After storms, check ceilings and closets for new stains.</li>
          </ol>

          <h2>Request a mold remediation referral</h2>
          <p>Call {CALL}. There is no fee to use this referral line. We help connect you with an independent provider serving Rio Rancho and nearby communities. Hiring decisions remain yours. Still have active water? Start with <a href="water-damage-restoration.html">water damage restoration</a>.</p>
''',
    "faqs": [
        ("How big an area needs a professional?",
         "U.S. EPA guidance suggests professional help for areas larger than about 10 square feet, for mold in HVAC systems, or for mold tied to sewage or contaminated water."),
        ("Is bleach enough?",
         "It may help on small areas of hard surfaces, but it does not fix the moisture problem and is not recommended for porous materials like drywall."),
    ],
})

site.service_page({
    "file": "fire-smoke-damage.html",
    "title": "Fire & Smoke Damage Restoration Referral | Rio Rancho, NM",
    "meta": "Kitchen fire, soot, smoke odor, or water from firefighting in Rio Rancho? Call free to connect with independent fire and smoke restoration providers.",
    "crumb": "Fire &amp; Smoke Damage",
    "h1": "Fire &amp; Smoke Damage Restoration",
    "lead": "After a fire, smoke, soot, and the water used to put it out often cause more damage than the flames. We connect Rio Rancho homeowners with independent providers who clean, deodorize, and dry fire-damaged homes.",
    "schema_name": "Fire and Smoke Damage Restoration Referral",
    "service_type": "Fire and smoke damage restoration",
    "schema_desc": "Free referral for fire, smoke, and soot damage restoration in Rio Rancho, New Mexico.",
    "side_h": "Had a fire?",
    "side_p": "Make sure the fire department has cleared the home, then call.",
    "body": '''          <p><strong>If anything is still burning, call 911 first.</strong> This page is about what comes after the fire is out and the fire department says the home is safe to enter.</p>

          <p>Even a small kitchen, dryer, or fireplace fire can spread soot through the HVAC system and leave smoke odor in carpet, cabinets, and clothing. Larger fires add a second problem: water. Hoses can soak floors, walls, and contents, and that water needs the same fast drying as any other <a href="water-damage-restoration.html">water damage</a>.</p>

          <h2>What fire restoration usually covers</h2>
          <ul>
            <li>Boarding up broken windows and tarping roof openings</li>
            <li>Removing water left by firefighting and drying the structure</li>
            <li>Soot cleanup on walls, ceilings, cabinets, and belongings</li>
            <li>Odor treatment, which may include air scrubbers or other deodorizing methods</li>
            <li>HVAC filter changes, duct cleaning, and evaporative cooler pad replacement when needed</li>
            <li>Inventory and pack-out of belongings for cleaning or claims</li>
          </ul>

          <h2>Wildfire smoke in New Mexico</h2>
          <p>New Mexico has seen very large wildfires. The 2011 Las Conchas Fire in the Jemez Mountains, which burned land in Sandoval County, grew to more than 156,000 acres, and the 2022 Calf Canyon/Hermits Peak Fire became the largest in state history at more than 340,000 acres. Even homes far from the flames can pick up smoke odor and fine ash, and evaporative coolers can pull smoky outdoor air straight inside. If smoke got into your home, a restoration provider can assess cleaning and odor treatment.</p>

          <h2>Do’s and don’ts after a fire</h2>
          <ul>
            <li><strong>Do</strong> wait for the fire department to say the home is safe.</li>
            <li><strong>Do</strong> photograph damage before cleaning anything.</li>
            <li><strong>Do</strong> contact your insurer early; fire losses usually involve an adjuster.</li>
            <li><strong>Don’t</strong> wipe soot off walls with a wet rag; it can smear and set the stain.</li>
            <li><strong>Don’t</strong> run the furnace, AC, or swamp cooler until filters, pads, and ducts are checked.</li>
            <li><strong>Don’t</strong> eat food or use medicine that was exposed to heat, smoke, or soot.</li>
          </ul>

          <h2>Get a referral</h2>
          <p>Call {CALL}. Tell us what burned, how much of the home has smoke or soot, and whether water was used to put it out. We will try to connect you with an independent fire restoration provider. Wet materials left behind can lead to <a href="mold-remediation.html">mold</a>, so ask about drying too.</p>
          <p class="source-note">Sources: National Park Service and USGS (Las Conchas Fire); Albuquerque Journal, “The 5 largest wildfires in New Mexico history” (Calf Canyon/Hermits Peak Fire).</p>
''',
    "faqs": [
        ("Can smoke odor be removed?",
         "Often, yes, but it usually takes more than air fresheners. Providers clean soot from surfaces and use deodorizing equipment. Some heavily affected materials need to be replaced."),
        ("Why is there water damage after a fire?",
         "Firefighting water can soak a home. That water needs to be extracted and dried quickly like any other water loss."),
    ],
})

# ======================= SERVICE AREAS =======================
areas_inner = '''          <p>When you call, tell us your city, neighborhood, or a cross street. We use that to connect you with an independent provider who serves your area when one is available.</p>

          <h2>Primary focus: Rio Rancho</h2>
          <p>Rio Rancho, in ZIP codes <strong>87124</strong> and <strong>87144</strong>, is our main coverage city. That includes established areas as well as newer neighborhoods across the city. Whether you are dealing with a monsoon roof leak in Enchanted Hills, a water heater failure near Northern Meadows, or a cooler overflow in Cabezon, you can call the same referral number.</p>
          <ul class="area-list">
            <li>Enchanted Hills</li>
            <li>Cabezon</li>
            <li>Northern Meadows</li>
            <li>Loma Colorado</li>
            <li>Riverview</li>
            <li>Along Unser Blvd</li>
            <li>Along NM 528</li>
          </ul>

          <h2>Nearby communities</h2>
          <ul class="area-list">
            <li>Corrales</li>
            <li>Bernalillo</li>
            <li>Placitas</li>
            <li>Northwest Albuquerque</li>
            <li>Paradise Hills area</li>
            <li>Taylor Ranch area</li>
            <li>Los Ranchos (nearby)</li>
          </ul>

          <h2>Near an arroyo?</h2>
          <p>Rio Rancho, Corrales, and Bernalillo are served by the Southern Sandoval County Arroyo Flood Control Authority (SSCAFCA), which publishes an interactive map of arroyo erosion hazard areas. FEMA’s Flood Map Service Center shows mapped floodplains. Both are worth checking if your home is close to an arroyo.</p>

          <h2>What “service area” means for a referral site</h2>
          <p>We are not a contractor with a fixed truck radius. We run a phone referral connection. The independent provider you speak with sets their own travel area, schedule, and fees. If a provider cannot take your job, you can ask about alternatives when you call.</p>

          <h2>Outside these areas?</h2>
          <p>If you are elsewhere in the Albuquerque metro or broader New Mexico, you are still welcome to call. We will be honest if we cannot help with a connection for your location.</p>

          <div class="notice">
            <strong>Note:</strong> Listing a community here does not guarantee a provider is available at the moment you call. Availability depends on network coverage and the independent companies participating at that time.
          </div>'''
site.simple_page("service-areas.html", "Service Areas | Rio Rancho Water Damage Referral",
                 "We connect homeowners in Rio Rancho (87124, 87144), Corrales, Bernalillo, Placitas, and Northwest Albuquerque with independent restoration providers.",
                 "Service Areas", "Service Areas",
                 "Our free referral line focuses on Rio Rancho and nearby communities in Sandoval County and Northwest Albuquerque. Provider availability can vary by day and by exact location.",
                 areas_inner, prio="0.7", freq="monthly", with_side=True,
                 side_h="Call for your area", side_p="Rio Rancho &amp; nearby")

# ======================= ABOUT =======================
about_inner = '''        <h2>Who we are</h2>
        <p>Rio Rancho Water Damage is a <strong>free referral / connection service</strong>. We are not a restoration contractor, mold remediator, fire restoration company, plumber, roofer, or insurance agency. We do not send technicians, submit insurance claims for you, or perform cleanup work.</p>
        <p>When you call {CALL}, your call may be connected or forwarded to an independent, licensed service provider who works in or near your area. That provider is a separate business. Any agreement you make is between you and them.</p>

        <h2>Why a referral site?</h2>
        <p>Searching online during an emergency is overwhelming. Many results mix national call centers, ads, and local companies without explaining who will actually show up. Our goal is simpler: give Rio Rancho-area homeowners one straightforward number to call about water extraction and drying, flood cleanup, sewage backups, mold, or fire and smoke damage.</p>

        <h2>What we provide</h2>
        <ul>
          <li>Educational pages about common water, mold, sewage, and fire damage situations</li>
          <li>A phone number you can call for a referral connection</li>
          <li>Clear disclosure that we are not the contractor</li>
        </ul>

        <h2>What we do not provide</h2>
        <ul>
          <li>On-site restoration, construction, roofing, plumbing, or mold removal</li>
          <li>Guarantees about response time, pricing, or insurance coverage</li>
          <li>Medical advice about mold, sewage, or smoke exposure</li>
          <li>A physical storefront for walk-in visits</li>
        </ul>

        <h2>Honesty matters</h2>
        <p>We do not invent reviews, licenses, certifications, or years in business for this site. We do not use someone else’s business name or address. Ask any provider you speak with directly about their credentials, insurance, and experience.</p>

        <h2>Questions about the site?</h2>
        <p>For referral calls, use {CALL}. For website or privacy questions, see our <a href="contact.html">Contact</a>, <a href="privacy.html">Privacy Policy</a>, and <a href="terms.html">Terms of Use</a> pages.</p>'''
site.simple_page("about.html", "About This Referral Service | Rio Rancho Water Damage",
                 "Learn how this free Rio Rancho water damage referral site works and what we do, and do not, provide.",
                 "About", "About This Referral Service",
                 "We built this site to help homeowners facing water, mold, sewage, or fire damage find a clear next step: a phone conversation with an independent local provider.",
                 about_inner, prio="0.5")

# ======================= CONTACT =======================
contact_inner = f'''        <div class="card" style="text-align:center;padding:2.5rem 1.5rem">
          <h2 class="mt-0">Free referral line</h2>
          <p>For water damage, monsoon and roof leaks, flood cleanup, burst pipes and slab leaks, sewage backups, mold, or fire and smoke damage in the Rio Rancho area:</p>
          <p style="font-size:1.75rem;font-weight:800;margin:1rem 0">
            <a class="phone-link" href="tel:{PHONE_TEL}">{PHONE_DISP}</a>
          </p>
          <a class="btn btn-primary btn-lg" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a>
          <p class="muted" style="margin-top:1.5rem;margin-bottom:0">Tap the button on a mobile phone to dial automatically.</p>
        </div>
        <div class="notice" style="margin-top:1.5rem">
          <strong>Reminder:</strong> This is a referral connection service. Calls may be forwarded to an independent provider. We do not have a public walk-in office.
        </div>
        <h2>Before you call, it helps to know</h2>
        <ul>
          <li>Your city or neighborhood and nearest cross street</li>
          <li>What caused the problem, if you know (storm, pipe, cooler, drain, fire)</li>
          <li>Which rooms are affected</li>
          <li>Whether water is still flowing, and whether it could be sewage</li>
        </ul>'''
site.simple_page("contact.html", "Contact | Rio Rancho Water Damage Referral",
                 "Call our free Rio Rancho water damage referral line. Phone contact only, no form required.",
                 "Contact", "Contact",
                 "The fastest way to reach us is by phone. There is no contact form on this site.",
                 contact_inner, prio="0.6")

site.legal_pages("November 11, 2026")
site.write()
