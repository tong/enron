# Enron
Zero cost s/css library

Every module only defines variables, functions and mixins: `@use` emits no CSS until you `@include` something.

```scss
@use 'enron/break';
@use 'enron/elevate';
@use 'enron/animation/fade';

@include fade.in;                       // @keyframes fade_in
@include fade.in($from: .5, $name: half); // @keyframes half

.card {
    @include elevate.elevate-2;
    @include break.min(md) { padding: 2rem; }
}
```

| Module | |
|---|---|
| `animation/*` | Keyframe mixins (attention, bounce, fade, flip, hinge, lightspeed, zoom). Every mixin takes a `$name` for the keyframes. |
| `effect/filmgrain`, `effect/underline` | Film grain overlay, link underline hover effects |
| `hamburger`, `hamburger/*` | Hamburger menu button: `@include hamburger.base;` plus variants like `@include slider.styles;` |
| `background`, `pattern` | CSS gradient backgrounds and patterns |
| `break` | Breakpoint media queries (`min`, `max`, `minmax`) |
| `media` | Expression based media queries, `@include media.query('>phone', '<=tablet')` |
| `ease`, `elevate`, `filter`, `glyph`, `z-index` | Constants and presets |
| `font`, `typography`, `golden-ratio` | `@font-face`, font weights, px to rem, golden ratio type sizes |
| `grid`, `layout`, `link`, `print` | Layout helpers |
| `string`, `unit` | String and unit functions |

## Development

```sh
npm test       # compile test/smoke.scss, which calls every mixin
npm run build  # compile index.scss
npm run build:example  # compile example/main.scss, then open example/index.html
```
