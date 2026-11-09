# rioranchowaterdamage.com

Static referral site (HTML/CSS) for GitHub Pages.

## Before going live

1. Buy a NumberBarn (or similar) number and run:
   ```bash
   ./replace_phone.sh "(505) XXX-XXXX" 505XXXXXXX
   ```
2. Point the domain DNS to GitHub Pages (A records / CNAME as usual).
3. Upload this folder to a public GitHub repo and enable Pages (root).
4. Confirm the `CNAME` file still contains `rioranchowaterdamage.com`.

## Honesty rules baked in

- Site is a **referral connection service**, not a contractor.
- Footer disclosure on every page.
- No fake address, reviews, licenses, or guarantees.
- Contact is phone-only (no form).

## Regenerate pages

```bash
python3 _build.py
```
Then re-run `replace_phone.sh` if placeholders were restored.
