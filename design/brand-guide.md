# edit.ac visual identity

Status: accepted artwork selected by the user on 2026-10-12. Owner: website and editor maintainers.

<p align="center"><img src="assets/editac-github-avatar.png" alt="edit.ac logo: a text cursor inside a square frame" width="160"></p>

## Mark and usage

The editor mark is the supplied text cursor inside a square frame. Preserve both original paths, including the frame. Use **edit.ac** as the visible name and place the mark to its left in a lockup. Keep the mark square, unrotated and free of added effects. Leave at least one frame-stroke width of clear space around it and render it at 16 CSS pixels or larger; the website header uses 32 pixels.

The styling follows Assign's current icon conventions, reviewed on 2026-10-12: a transparent one-color product mark, a browser-scheme-aware transparent favicon, and opaque padded artwork for external listings and install icons. Browser favicons follow `prefers-color-scheme`; the product logo follows the selected interface foreground. Earlier Assign guidance about a white favicon tile was superseded on 2026-09-27.

Use Oil black `#0c0c0c` on light surfaces and white or the current light foreground on dark surfaces. Maintain at least 3:1 contrast with the surrounding surface. Product logos inherit the interface foreground; avoid embedded fixed backgrounds there. When visible edit.ac text accompanies the mark, treat it as decorative. A standalone logo link needs the accessible name **edit.ac**.

## Asset ownership

The [docs repository's brand directory](https://github.com/edit-ac/docs/tree/main/static/brand) owns the source and generated artwork. The [editor mark](assets/editac-mark.svg) and preview beside this guide are byte-identical copies. The core repository keeps the same copies in `brand/` for editor consumers and its repository README.

| Surface | Asset | Treatment |
| --- | --- | --- |
| Editor and site header | `brand/editac-mark.svg` | Unchanged geometry, transparent; use a CSS mask or inline paths to inherit foreground |
| Browser tab | `favicon.svg` | Transparent with a small clear-space margin; Oil black in light browser chrome, white in dark chrome |
| Legacy favicon | `favicon.ico` | 16, 32 and 48 pixel fallbacks with an opaque white surface |
| GitHub organization | `brand/editac-github-avatar.png` | 1024 × 1024, Oil black on white; mark occupies the central two-thirds and fits a circular crop |
| Touch and install artwork | `brand/editac-app-icon.svg`, `editac-app-icon-{180,192,512}.png` | Same padded white canvas; 180 pixel artwork is linked as the site's Apple touch icon |

The PNG assets are prepared for their stated uses. The docs site has no PWA manifest; these assets do not add installation or native-package support.

## Reproduction and maintenance

Run `node scripts/generate-brand.mjs` in the docs repository with `rsvg-convert` and ImageMagick's `magick` available. The generator reads `editac-source.svg`, preserves its two path definitions, and changes only fill, padding and output format. Commit generated outputs with any source change. Copy `editac-mark.svg` and `editac-github-avatar.png` to this guide's `assets/` directory and core's `brand/`, then confirm the copies match with `cmp`.

Keep website overrides outside the DevLab submodule. Check header readability in light, dark and system modes; inspect home, docs, search and narrow navigation. Confirm the favicon switches with browser preference independently of the website theme, the raster dimensions match their names, and circular cropping preserves the GitHub mark.

## Provenance

The user supplied `edit-text-edit-tools-svgrepo-com.svg`. [SVG Repo's source page](https://www.svgrepo.com/svg/238902/edit-text-edit-tools) identifies **Edit Text Edit Tools** as CC0 artwork, uploaded by SVG Repo. Keep the original file and provenance in the canonical brand directory. Artwork reuse does not establish trademark registration or clearance.
