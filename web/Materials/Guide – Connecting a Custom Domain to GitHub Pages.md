# Guide: Connecting a Custom Domain to GitHub Pages

## What you have
- Repository: `https://github.com/heavymetalmax/waste`
- Site currently available at: `https://heavymetalmax.github.io`
- Goal: connect `biotc.pl` (or another domain)

---

## Step 1 — Buy a domain

Recommended registrars:

| Registrar | .pl domains | Link |
|---|---|---|
| OVH | ~40 PLN/year | ovh.pl |
| Namecheap | ~15 $/year | namecheap.com |
| Domeny.pl | ~30–50 PLN/year | domeny.pl |

Provide any email address during registration — you will need it to manage the domain.

---

## Step 2 — Configure DNS at your registrar

After purchasing the domain, go to your registrar's DNS management panel and add **4 A records** and **1 CNAME record**:

### A records (for the apex domain `biotc.pl`)

| Type | Name | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |

### CNAME record (for `www.biotc.pl`)

| Type | Name | Value |
|---|---|---|
| CNAME | www | heavymetalmax.github.io |

> **Note:** DNS changes propagate within 30 minutes to 48 hours.

---

## Step 3 — Configure GitHub Pages

1. Open: `https://github.com/heavymetalmax/waste/settings/pages`
2. Under **"Custom domain"** enter: `biotc.pl`
3. Click **Save**
4. Check **"Enforce HTTPS"** (this option appears ~10 minutes after saving)

GitHub will automatically:
- Create a `CNAME` file in the repository
- Issue a free SSL certificate (Let's Encrypt)

---

## Step 4 — Update links in the codebase

After connecting the domain, a few things in the code need to be updated:

### 4.1 `build.py` — hreflang links
The templates in `biotc/index.html` contain lines like:
```html
<link rel="alternate" hreflang="uk-UA" href="https://biotc.com.ua/" />
```
Replace `biotc.com.ua` with your actual domain.

### 4.2 Generate `sitemap.xml`
Once the domain is live — ask Claude Code and it will generate it automatically.

### 4.3 Google Search Console
Register the domain at `search.google.com/search-console` to allow Google to index the site.

---

## Verification

1–24 hours after completing all steps:

1. Open `https://biotc.pl` — your site should appear
2. Open `https://www.biotc.pl` — should redirect to `biotc.pl`
3. A padlock icon 🔒 should be visible in the address bar (HTTPS)

---

## Troubleshooting

**Site not loading after 24 hours:**
- Check the A records in your DNS panel (exactly the 4 GitHub IP addresses)
- Confirm that your domain is entered in GitHub Settings → Pages

**HTTPS not working:**
- Click "Enforce HTTPS" again in GitHub Settings → Pages
- Wait another 10 minutes

**Questions:** contact Claude Code with the error message you see.

---

*Time required: ~20 minutes of work + up to 24 hours for DNS propagation*
