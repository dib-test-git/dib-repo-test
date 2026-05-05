# PARTSTORE

Al-Bahar's 24×7 online CAT parts ordering portal — this directory holds the in-progress rewrite for the GCC market. Tracked by epic #7.

## What's in this PR

Arabic localization foundation (closes #12):

- Base message catalog for `en` and `ar`
- `direction()` helper that returns `rtl` for Arabic
- `LocaleToggle` component for the language switch

Part numbers and Cat-supplied product descriptions deliberately stay in English — we only translate the UI shell.

## Next up

- RTL CSS logical-properties audit (separate PR)
- Arabic email templates for order confirmations
- Automated visual regression tests for RTL layout
