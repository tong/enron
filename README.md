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
| `animation/*` | Keyframe mixins (attention, bounce, fade, flip, hinge, lightspeed, rotate, slide, zoom). Every mixin takes a `$name` for the keyframes. |
| `animate` | `animate.play($name, ...)` plays keyframes, respecting reduced motion |
| `effect/filmgrain`, `effect/underline` | Film grain overlay, link underline hover effects |
| `hamburger`, `hamburger/*` | Hamburger menu button: `@include hamburger.base;` plus variants like `@include slider.styles;` |
| `a11y` | `visually-hidden`, `visually-hidden-focusable`, `focus-visible`, `reduced-motion`, `motion` |
| `color` | `tint`, `shade`, `palette`, `luminance`, `contrast`, `text-color` |
| `spacing`, `fluid` | Spacing scale `spacing.space(2, 4)`, viewport based `clamp()` values `fluid.value(1rem, 2rem)` |
| `background`, `pattern` | CSS gradient backgrounds and patterns |
| `break` | Breakpoint media queries (`min`, `max`, `minmax`) |
| `media` | Expression based media queries, `@include media.query('>tablet', 'dark')`. Uses the `break` breakpoints |
| `glyph` | 431 characters for `content`, by Unicode name (`$black-star`) and HTML entity name (`$hearts`) |
| `ease`, `elevate`, `filter`, `z-index` | Constants and presets, `elevate.elevate($level)`, named layers `z-index.layer(modal)` |
| `font`, `typography`, `golden-ratio` | `@font-face`, font weights, px to rem, golden ratio type sizes |
| `grid`, `layout`, `link`, `print` | Layout helpers: `center`, `stack`, `cluster`, `line-clamp`, `aspect-ratio`, `grid.auto-fill`, `grid.columns`, ... |
| `string`, `unit` | String and unit functions, `unit.strip-unit` |

## Development

```sh
npm test       # compile test/smoke.scss, which calls every mixin
npm run build  # compile index.scss
npm run build:example  # compile example/main.scss, then open example/index.html
```
