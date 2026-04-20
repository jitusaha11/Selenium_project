# PAP-177 — Grunt handoff for Pedant

## What I changed
- Added a new semantic app download section to `index.html` below the existing overview card grid.
- Added CTA copy, two store-style download buttons, and a CSS-only mobile mockup preview.
- Added dedicated app-download CSS in `styles.css` for:
  - `.app-download`
  - `.app-download__content`
  - `.app-download__title`
  - `.app-download__text`
  - `.app-download__actions`
  - `.app-download__preview`
  - `.app-mockup` and its child elements
  - `.store-button` and its child elements
- Reused existing theme variables so dark/light mode stays consistent.
- Added subtle hover/focus states for the download buttons.
- Ensured the section stacks cleanly on narrower screens and buttons wrap/full-width on mobile.

## Files changed
- `index.html`
- `styles.css`
- `GRUNT_HANDOFF_PAP-177.md`

## Things to verify
- App download section appears below the overview cards.
- Section contains heading, supporting text, two download buttons, and a preview mockup.
- Button hover and focus states are visible and consistent.
- Layout becomes single-column on narrower screens.
- Buttons expand cleanly on mobile without overflow.
- Mockup remains decorative and visually balanced in both themes.
- Existing sidebar and overview cards remain visually unaffected.

## Notes
- No JavaScript added.
- No git push or PR actions performed.
- The architect artifact was not present in this checkout snapshot, so implementation followed the ticket and current UI patterns.
