# SEO & GA4 Setup — sabinelindeberg.dk

## Deployed: 2026-03-05

### Summary
Complete SEO package and GA4 setup for **sabinelindeberg.dk** (Indre Kald og Kraft — Sabine Lindeberg, Hypnoseterapeut). All 6 HTML pages now have:
- ✅ Canonical tags
- ✅ GA4 gtag.js snippet (placeholder)
- ✅ Structured data (JSON-LD)
- ✅ Sitemap.xml
- ✅ robots.txt

---

## Files Created

### 1. **sitemap.xml**
Location: `/sitemap.xml`

Includes all 6 pages with proper priorities:
- `index.html` → priority 1.0 (homepage)
- Service pages (hypnoseterapi, terapeutisk-samtale, shamanistiske-cirkler) → priority 0.8
- Other pages (om-sabine, kontakt) → priority 0.7
- All with lastmod: 2026-03-05

**Usage:** Submit to Google Search Console after domain verification.

### 2. **robots.txt**
Location: `/robots.txt`

```
User-agent: *
Allow: /

Sitemap: https://sabinelindeberg.dk/sitemap.xml
```

Allows all crawlers and references sitemap.

### 3. **seo-inject.py**
Location: `/seo-inject.py`

Python script for managing SEO tags across all HTML files.

**Features:**
- Injects canonical tags
- Injects GA4 gtag.js snippet
- Injects appropriate JSON-LD schemas per page type
- Checks for duplicates (won't inject if canonical already exists)

**Usage:**
```bash
python3 seo-inject.py
```

**Configuration (editable in script):**
- `BASE_URL`: https://sabinelindeberg.dk
- `BUSINESS_NAME`: "Indre Kald og Kraft — Sabine Lindeberg"
- `BUSINESS_EMAIL`: sabinelindeberg@hotmail.com
- `LOCATION`: Frederikssund, Denmark
- `GA4_ID`: G-XXXXXXXXXX (placeholder — update after GA4 property creation)
- `IMAGE_URL`: https://sabinelindeberg.dk/materiale/sabine-portrait.jpg

---

## HTML Files Updated

All 6 pages now have canonical tags, GA4 snippet, and JSON-LD schemas injected:

### 1. **index.html**
- **Schema Type:** LocalBusiness
- **Canonical:** https://sabinelindeberg.dk/
- **Includes:** Business name, email, location, image, type

### 2. **hypnoseterapi.html**
- **Schema Type:** Service
- **Canonical:** https://sabinelindeberg.dk/hypnoseterapi.html
- **Includes:** Service name, description, provider details, service area

### 3. **terapeutisk-samtale.html**
- **Schema Type:** Service
- **Canonical:** https://sabinelindeberg.dk/terapeutisk-samtale.html
- **Includes:** Service name, description, provider details, service area

### 4. **shamanistiske-cirkler.html**
- **Schema Type:** Service
- **Canonical:** https://sabinelindeberg.dk/shamanistiske-cirkler.html
- **Includes:** Service name, description, provider details, service area

### 5. **om-sabine.html**
- **Schema Type:** AboutPage
- **Canonical:** https://sabinelindeberg.dk/om-sabine.html
- **Includes:** Person details (Sabine Lindeberg), job title, image, description

### 6. **kontakt.html**
- **Schema Type:** ContactPage
- **Canonical:** https://sabinelindeberg.dk/kontakt.html
- **Includes:** Contact information, business details, address

---

## GA4 Setup Instructions

### Step 1: Create GA4 Property
1. Go to https://analytics.google.com
2. Sign in as **steven@bygmedai.dk**
3. Create new property named: **"Indre Kald og Kraft — sabinelindeberg.dk"**
4. Select **Denmark** as location
5. Complete setup — you'll receive a GA4 ID like: `G-XXXXXXXXXX`

### Step 2: Update GA4 ID
Once you have the GA4 ID, update the placeholder in all HTML files:

**Option A: Manual**
Find and replace in all 6 HTML files:
```
G-XXXXXXXXXX  →  [Your actual GA4 ID]
```

**Option B: Automated (recommended)**
1. Edit `/seo-inject.py` line: `GA4_ID = "G-XXXXXXXXXX"`
2. Replace placeholder with actual ID
3. Run: `python3 seo-inject.py`
4. Commit and push changes

### Step 3: Verify Tracking
1. Go to GA4 property
2. Select **Real-time** in left menu
3. Open https://sabinelindeberg.dk/ in a new browser
4. Verify traffic appears in Real-time view (may take 30 seconds)

### Step 4: Create Events (Optional)
Suggested custom events for tracking customer journeys:
- `contact_form_submit` — when kontakt.html form is submitted
- `service_click` — when user clicks on a service page
- `phone_click` — when user clicks phone number
- `email_click` — when user clicks email address

---

## Google Search Console Setup

### Step 1: Verify Domain Ownership
1. Go to https://search.google.com/search-console
2. Add property for **https://sabinelindeberg.dk/**
3. Verify via HTML tag (recommended) or DNS record
4. Copy verification tag and add to `<head>` of index.html (or use GitHub Pages verification via DNS)

**Alternative (DNS verification — faster for GitHub Pages):**
- GitHub Pages automatically handles HTTPS verification via DNS

### Step 2: Submit Sitemap
1. In Search Console, go to **Sitemaps** (left menu)
2. Enter: `https://sabinelindeberg.dk/sitemap.xml`
3. Click Submit

### Step 3: Check Coverage
1. Go to **Coverage** (left menu) after 24-48 hours
2. Verify all 6 pages are indexed

### Step 4: Monitor Performance
- **Performance** tab shows clicks, impressions, CTR, position for search results
- **Experience** tabs show Core Web Vitals
- **Enhancements** show structured data validation (JSON-LD schemas)

---

## JSON-LD Schemas Explained

### LocalBusiness (index.html)
Tells Google that this is a local business offering services.
```json
{
  "@type": "LocalBusiness",
  "name": "Indre Kald og Kraft — Sabine Lindeberg",
  "address": {"addressLocality": "Frederikssund", "addressCountry": "DK"},
  "email": "sabinelindeberg@hotmail.com"
}
```

### Service (hypnoseterapi, terapeutisk-samtale, shamanistiske-cirkler)
Tells Google what services are offered.
```json
{
  "@type": "Service",
  "name": "[Service Name]",
  "provider": {"@type": "LocalBusiness", ...},
  "areaServed": "Frederikssund, Denmark"
}
```

### AboutPage (om-sabine.html)
Tells Google who is behind the business.
```json
{
  "@type": "AboutPage",
  "mainEntity": {
    "@type": "Person",
    "name": "Sabine Lindeberg",
    "jobTitle": "Hypnoseterapeut og Visdomsformidler"
  }
}
```

### ContactPage (kontakt.html)
Tells Google this is the contact page.
```json
{
  "@type": "ContactPage",
  "mainEntity": {"@type": "LocalBusiness", ...}
}
```

---

## Checklist: Next Steps

- [ ] Create GA4 property under steven@bygmedai.dk
- [ ] Replace G-XXXXXXXXXX with actual GA4 ID
- [ ] Verify domain in Google Search Console (DNS or HTML tag)
- [ ] Submit sitemap.xml to GSC
- [ ] Check robots.txt in GSC
- [ ] Wait 24-48 hours for indexing
- [ ] Monitor Coverage and Performance in GSC
- [ ] Set up GA4 custom events (optional but recommended)

---

## Technical Details

### Canonical Tag
Placed immediately after `<head>` opening tag:
```html
<link rel="canonical" href="https://sabinelindeberg.dk/[page].html">
```
Prevents duplicate content issues and consolidates SEO signals to main URL.

### GA4 gtag.js
Placed in `<head>` section:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```
Tracks all pageviews, user engagement, and conversions.

### JSON-LD Schemas
Placed in `<script type="application/ld+json">` tags:
- Helps search engines understand page content
- Improves rich snippets in search results
- No visual impact on website

---

## Questions or Updates?

For updating GA4 ID or modifying schemas:
1. Edit `/seo-inject.py` configuration
2. Run: `python3 seo-inject.py`
3. Commit and push: `git add . && git commit -m "Update GA4 ID" && git push`

For manual schema updates, edit JSON directly in HTML `<head>` section.

---

**Status:** ✅ Complete and deployed
**Commit:** b63ce40
**Date:** 2026-03-05
