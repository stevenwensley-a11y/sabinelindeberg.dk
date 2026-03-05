# GA4 Setup Quick Start — sabinelindeberg.dk

**For Steven Wensley**

## What's Already Done ✅

All 6 pages on your website now have:
- Canonical tags (prevent duplicate indexing)
- Google Analytics code (ready to track visitors)
- Structured data (help Google understand your business)

**You just need to:**
1. Create a GA4 property
2. Update the placeholder code with your real GA4 ID

## Step-by-Step (5 minutes)

### 1. Create GA4 Property

1. Go to https://analytics.google.com
2. Click **Create** (or + sign if you already have properties)
3. Select **Web**
4. Name: `Indre Kald og Kraft — sabinelindeberg.dk`
5. Click **Create**
6. For data collection:
   - Website URL: `https://sabinelindeberg.dk`
   - Country: `Denmark`
   - Timezone: `Europe/Copenhagen`
   - Industry category: `Professional Services` (or `Wellness & Beauty`)
   - Business size: `Small`
7. Accept terms and complete setup
8. **Copy your GA4 ID** (looks like: `G-XXXXXXXXXX`)

### 2. Update the Placeholder

1. Open `/seo-inject.py` in GitHub (github.com/stevenwensley-a11y/sabinelindeberg.dk)
2. Click the pencil icon to edit
3. Find this line (around line 16):
   ```python
   GA4_ID = "G-XXXXXXXXXX"
   ```
4. Replace `G-XXXXXXXXXX` with your actual GA4 ID
5. Commit the change

### 3. Run the Update Script

In your terminal:
```bash
python3 /path/to/seo-inject.py
```

This will inject your real GA4 ID into all 6 HTML pages.

### 4. Deploy

```bash
git add .
git commit -m "Update GA4 ID to G-XXXXXXXXXX"
git push origin main
```

### 5. Verify Tracking

1. Go back to GA4 (https://analytics.google.com)
2. Click **Real-time** (in the left menu)
3. Open https://sabinelindeberg.dk in a new browser tab
4. You should see yourself in the Real-time view (30-second delay is normal)

## Done! 🎉

Your website is now tracking visitors.

**Next:** Submit your website to Google Search Console (see SEO-GA4-DOCUMENTATION.md for full guide).

---

## Troubleshooting

**GA4 traffic not showing?**
- Wait 30-60 seconds
- Make sure you're in an incognito/private browser window (GA4 filters some bots)
- Check that GA4 ID is correctly formatted in the script

**Can't find your GA4 ID?**
- In Google Analytics, click the gear icon (Settings) at the bottom left
- Go to **Property Settings**
- Scroll to **Google Analytics 4 properties** section
- Your ID should be visible at the top

**Questions?**
- See SEO-GA4-DOCUMENTATION.md for the full guide
- GA4 support: https://support.google.com/analytics

