# rioranchowaterdamage.com (v2)

Static referral site (HTML/CSS) for GitHub Pages. v2 adds seven service pages, a Services dropdown,
an emergency banner, related-service links, per-page FAQs, and breadcrumb schema.

All v1 URLs still exist as full pages (flood-cleanup.html and burst-pipe-leak.html were kept and expanded),
so no redirects are needed. New pages: storm-roof-leak-damage.html, sewage-backup-cleanup.html, fire-smoke-damage.html.

## Before going live

1. Buy a NumberBarn (or similar) number and run:
   ```bash
   ./replace_phone.sh "(505) XXX-XXXX" 505XXXXXXX
   ```
2. Point the domain DNS to GitHub Pages (A records / CNAME as usual).
3. Upload this folder to the GitHub repo and enable Pages (root). Keep `.nojekyll`.
4. Confirm the `CNAME` file still contains `rioranchowaterdamage.com`.

## Honesty rules baked in

- Site is a **referral connection service**, not a contractor.
- Footer disclosure + per-page referral disclosure on every service page.
- No address, reviews, licenses, years in business, or guarantees.
- "Call any time" wording is paired with "provider availability varies". Keep 24/7 wording only if the number really routes 24/7.
- Contact is phone-only (no form).

## Regenerate pages

```bash
python3 _build.py   # uses _sitekit.py (shared templates)
```
Then re-run `replace_phone.sh` if placeholders were restored.
