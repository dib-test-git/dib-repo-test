# Rental Portal

Customer self-service portal for Al-Bahar equipment rentals across UAE, Kuwait, Qatar, Oman, and Bahrain.

## Status

Initial scaffold — replaces the phone/email-based reservation workflow. Tracked by issue #8 under the Rental Fleet Digital Platform milestone.

## Stack (proposed)

- Next.js 14 (App Router) for the frontend
- Node.js API layer calling the existing ERP
- i18n via `next-intl` (English first, Arabic to follow — see #12)

## Running locally

```bash
npm install
npm run dev
```

## Environment

| Variable | Description |
|---|---|
| `ERP_API_BASE` | Base URL for ERP rental APIs |
| `SMS_GATEWAY_KEY` | API key for Arabic-capable SMS provider |
| `PUBLIC_SITE_URL` | Canonical URL (country-specific CDN) |

## Directory layout

- `src/pages/` — Next.js route handlers
- `src/data/` — static catalog fixtures (to be replaced with live ERP calls)
