#!/usr/bin/env python3
"""
SEO Injection Script for sabinelindeberg.dk
Adds canonical tags, JSON-LD schemas, GA4 gtag.js, OG/Twitter meta tags to all HTML files.
"""

import re
import json
from pathlib import Path
from datetime import datetime

# Configuration
BASE_URL = "https://sabinelindeberg.dk"
BUSINESS_NAME = "Indre Kald og Kraft — Sabine Lindeberg"
BUSINESS_EMAIL = "sabinelindeberg@hotmail.com"
LOCATION = "Frederikssund, Denmark"
GA4_ID = "G-XXXXXXXXXX"  # Placeholder - will be replaced after property creation
IMAGE_URL = f"{BASE_URL}/materiale/sabine-portrait.jpg"

# Page configuration
PAGES = {
    "index.html": {
        "title": "Indre Kald og Kraft — Hypnoseterapi i Frederikssund",
        "description": "Find klarhed, retning og indre kraft. Hypnoseterapi, terapeutisk samtale og shamanistiske cirkler ved Sabine Lindeberg.",
        "url": f"{BASE_URL}/",
        "type": "LocalBusiness"
    },
    "hypnoseterapi.html": {
        "title": "Hypnoseterapi — Find Klarhed og Indre Styrke",
        "description": "Hypnoseterapi i Frederikssund. Løs negative mønstre og find ro gennem dyb, helende hypnose.",
        "url": f"{BASE_URL}/hypnoseterapi.html",
        "type": "Service"
    },
    "terapeutisk-samtale.html": {
        "title": "Terapeutisk Samtale — Mennesket i Centrum",
        "description": "Dybdesamtale i Frederikssund. Værdifuld terapi for dem, der søger indsigt og vejledning.",
        "url": f"{BASE_URL}/terapeutisk-samtale.html",
        "type": "Service"
    },
    "shamanistiske-cirkler.html": {
        "title": "Shamanistiske Cirkler — Forbindelse og Fællesskab",
        "description": "Shamanistiske cirkler i Frederikssund. Ritual, musik og spiralsamfund for kvinder der søger dybere forbindelse.",
        "url": f"{BASE_URL}/shamanistiske-cirkler.html",
        "type": "Service"
    },
    "om-sabine.html": {
        "title": "Om Sabine Lindeberg — Hypnoseterapeut og Visdomsformidler",
        "description": "Møt Sabine Lindeberg. 25+ års erfaring som terapeut, instruktør og vejleder i personlig udvikling.",
        "url": f"{BASE_URL}/om-sabine.html",
        "type": "AboutPage"
    },
    "kontakt.html": {
        "title": "Kontakt Sabine — Book Din Første Session",
        "description": "Kontakt Sabine Lindeberg i Frederikssund. Hypnoseterapi, terapeutisk samtale og shamanistiske cirkler.",
        "url": f"{BASE_URL}/kontakt.html",
        "type": "ContactPage"
    }
}

def generate_canonical_tag(url):
    """Generate canonical tag"""
    return f'  <link rel="canonical" href="{url}">'

def generate_ga4_snippet():
    """Generate GA4 gtag.js snippet"""
    return f'''  <!-- Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{GA4_ID}');
  </script>'''

def generate_localbusiness_schema(title, description, url):
    """Generate LocalBusiness JSON-LD schema"""
    schema = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": BUSINESS_NAME,
        "description": description,
        "url": url,
        "email": BUSINESS_EMAIL,
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Frederikssund",
            "addressCountry": "DK"
        },
        "image": IMAGE_URL
    }
    return f'''  <script type="application/ld+json">
{json.dumps(schema, indent=4, ensure_ascii=False)}
  </script>'''

def generate_service_schema(title, description, url):
    """Generate Service JSON-LD schema"""
    schema = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": title,
        "description": description,
        "provider": {
            "@type": "LocalBusiness",
            "name": BUSINESS_NAME,
            "url": BASE_URL,
            "email": BUSINESS_EMAIL
        },
        "image": IMAGE_URL,
        "areaServed": "Frederikssund, Denmark"
    }
    return f'''  <script type="application/ld+json">
{json.dumps(schema, indent=4, ensure_ascii=False)}
  </script>'''

def generate_aboutpage_schema(description, url):
    """Generate AboutPage JSON-LD schema"""
    schema = {
        "@context": "https://schema.org",
        "@type": "AboutPage",
        "name": "Om Sabine Lindeberg",
        "description": description,
        "url": url,
        "mainEntity": {
            "@type": "Person",
            "name": "Sabine Lindeberg",
            "jobTitle": "Hypnoseterapeut og Visdomsformidler",
            "image": IMAGE_URL
        }
    }
    return f'''  <script type="application/ld+json">
{json.dumps(schema, indent=4, ensure_ascii=False)}
  </script>'''

def generate_contactpage_schema(description, url):
    """Generate ContactPage JSON-LD schema"""
    schema = {
        "@context": "https://schema.org",
        "@type": "ContactPage",
        "name": "Kontakt",
        "description": description,
        "url": url,
        "mainEntity": {
            "@type": "LocalBusiness",
            "name": BUSINESS_NAME,
            "email": BUSINESS_EMAIL,
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Frederikssund",
                "addressCountry": "DK"
            }
        }
    }
    return f'''  <script type="application/ld+json">
{json.dumps(schema, indent=4, ensure_ascii=False)}
  </script>'''

def inject_seo_tags(filename):
    """Inject SEO tags into HTML file"""
    filepath = Path(filename)
    
    if not filepath.exists():
        print(f"❌ File not found: {filename}")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    page_config = PAGES.get(filename)
    if not page_config:
        print(f"⚠️  No config for {filename}, skipping")
        return False
    
    # Find the head section
    head_match = re.search(r'<head[^>]*>', content)
    if not head_match:
        print(f"❌ No <head> tag found in {filename}")
        return False
    
    # Find position right after charset/viewport
    head_start = head_match.end()
    
    # Find first meta tag or title to insert after
    insertion_point = head_start
    
    # Build SEO tags
    seo_tags = [
        generate_canonical_tag(page_config["url"]),
        ""
    ]
    
    # Add GA4
    seo_tags.append(generate_ga4_snippet())
    seo_tags.append("")
    
    # Add JSON-LD based on page type
    page_type = page_config["type"]
    if page_type == "LocalBusiness":
        seo_tags.append(generate_localbusiness_schema(page_config["title"], page_config["description"], page_config["url"]))
    elif page_type == "Service":
        seo_tags.append(generate_service_schema(page_config["title"], page_config["description"], page_config["url"]))
    elif page_type == "AboutPage":
        seo_tags.append(generate_aboutpage_schema(page_config["description"], page_config["url"]))
    elif page_type == "ContactPage":
        seo_tags.append(generate_contactpage_schema(page_config["description"], page_config["url"]))
    
    # Check if canonical already exists
    if 'rel="canonical"' in content:
        print(f"⚠️  Canonical tag already exists in {filename}, skipping injection")
        return False
    
    # Inject at head start
    seo_block = "\n".join(seo_tags)
    new_content = content[:insertion_point] + "\n" + seo_block + "\n" + content[insertion_point:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ SEO tags injected into {filename}")
    return True

def main():
    print("=" * 60)
    print("SEO Injection Script — sabinelindeberg.dk")
    print("=" * 60)
    print()
    
    success_count = 0
    for filename in PAGES.keys():
        if inject_seo_tags(filename):
            success_count += 1
    
    print()
    print("=" * 60)
    print(f"✅ Completed: {success_count}/{len(PAGES)} files updated")
    print("=" * 60)
    print()
    print("🔔 NEXT STEPS:")
    print("1. Create GA4 property under steven@bygmedai.dk account")
    print("2. Replace G-XXXXXXXXXX placeholder with actual GA4 ID")
    print("3. Submit sitemap.xml to Google Search Console")
    print("4. Verify robots.txt in GSC")

if __name__ == "__main__":
    main()
