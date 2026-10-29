import re, sys, unicodedata
from html.entities import codepoint2name

# Generates enron/_glyph.scss: every HTML 4 entity, grouped by Unicode block,
# named after its Unicode name, plus commonly used extras.
#
# Usage: python3 scripts/glyph.py enron/_glyph.scss > /tmp/_glyph.scss && mv /tmp/_glyph.scss enron/
# The current file is read to make sure no existing name goes missing.

old_src = open(sys.argv[1]).read()
old = {}
for m in re.finditer(r'^\$([A-Za-z][\w-]*)\s*:\s*([^;]+);', old_src, re.M):
    old[m.group(1).replace('_', '-')] = m.group(2).strip()

entities = dict(codepoint2name)
# HTML5 maps these to the mathematical angle brackets. 2329/232A (HTML 4) are still included, without entity name
del entities[0x2329], entities[0x232a]
entities[0x27e8] = 'lang'
entities[0x27e9] = 'rang'

def uname(cp):
    n = unicodedata.name(chr(cp)).lower()
    if ' letter ' in n:
        n = n.replace(' with ', ' ')
    for a, b in (('latin ', ''), ('greek ', ''), (' letter ', ' '), ('vulgar ', '')):
        n = n.replace(a, b)
    return re.sub(r'[^a-z0-9]+', '-', n).strip('-')

def lit(cp):
    return '"\\%04x"' % cp

ASCII_NAMES = {0x26: 'ampersand', 0x22: 'quotation-mark', 0x3c: 'less-than', 0x3e: 'greater-than'}

def r(a, b):
    return list(range(a, b + 1))

# (title, codepoints). Entities in these ranges are added automatically.
SECTIONS = [
    ('Special Characters', [0x22, 0x26, 0x3c, 0x3e]),
    ('Latin-1 Supplement', r(0xa0, 0xff)),
    ('Latin Extended', [0x152, 0x153, 0x160, 0x161, 0x178, 0x192]),
    ('Spacing Modifier Letters', [0x2c6, 0x2dc]),
    ('Greek', [c for c in r(0x391, 0x3a9) if c != 0x3a2] + r(0x3b1, 0x3c9) + [0x3d1, 0x3d2, 0x3d6]),
    ('General Punctuation', sorted(c for c in entities if 0x2000 <= c <= 0x206f) + [0x2010, 0x2011, 0x2012, 0x2015, 0x2016, 0x2027, 0x2030, 0x203b, 0x203c, 0x2047, 0x2048, 0x2049]),
    ('Currency Symbols', [0x20a9, 0x20aa, 0x20ac, 0x20b1, 0x20b9, 0x20ba, 0x20bd, 0x20bf]),
    ('Letterlike Symbols', [0x2103, 0x2109, 0x2111, 0x2113, 0x2116, 0x2117, 0x2118, 0x211c, 0x2120, 0x2122, 0x2126, 0x212e, 0x2135]),
    ('Number Forms', r(0x2153, 0x215e)),
    ('Arrows', r(0x2190, 0x2199) + [0x21a9, 0x21aa, 0x21b5, 0x21ba, 0x21bb, 0x21c4, 0x21c5, 0x21c6] + r(0x21d0, 0x21d4) + [0x21e7]),
    ('Mathematical Operators', sorted(c for c in entities if 0x2200 <= c <= 0x22ff) + [0x2213, 0x2216, 0x2218, 0x2219, 0x221b, 0x221c, 0x2223, 0x2226, 0x2236, 0x2247, 0x2249, 0x2260, 0x226a, 0x226b, 0x22c5, 0x27e8, 0x27e9]),
    ('Miscellaneous Technical', [0x2302, 0x2308, 0x2309, 0x230a, 0x230b, 0x2329, 0x232a, 0x2318, 0x231a, 0x231b, 0x2325, 0x2326, 0x2328, 0x232b, 0x23ce, 0x23cf, 0x23e9, 0x23ea, 0x23eb, 0x23ec, 0x23f0, 0x23f3, 0x23f8, 0x23f9, 0x23fa, 0x238b]),
    ('Geometric Shapes', [0x25a0, 0x25a1, 0x25aa, 0x25ab, 0x25b2, 0x25b3, 0x25b6, 0x25b7, 0x25bc, 0x25bd, 0x25c0, 0x25c1, 0x25c6, 0x25c7, 0x25ca, 0x25cb, 0x25cf, 0x25d0, 0x25d1, 0x25e6, 0x25ef]),
    ('Miscellaneous Symbols', [0x2600, 0x2601, 0x2602, 0x2603, 0x2605, 0x2606, 0x260e, 0x2610, 0x2611, 0x2612, 0x261c, 0x261d, 0x261e, 0x261f, 0x2620, 0x2622, 0x2623, 0x262f, 0x2630, 0x2639, 0x263a, 0x263c, 0x2640, 0x2642, 0x2660, 0x2661, 0x2662, 0x2663, 0x2664, 0x2665, 0x2666, 0x2667, 0x2669, 0x266a, 0x266b, 0x266c, 0x266d, 0x266e, 0x266f, 0x267b, 0x267f, 0x2690, 0x2691, 0x2693, 0x2696, 0x2699, 0x26a0, 0x26a1, 0x26aa, 0x26ab, 0x26d4]),
    ('Dingbats', [0x2702, 0x2709, 0x270e, 0x270f, 0x2712, 0x2713, 0x2714, 0x2715, 0x2716, 0x2717, 0x2718, 0x271a, 0x2726, 0x2727, 0x2731, 0x2733, 0x2734, 0x2744, 0x274c, 0x2753, 0x2757, 0x275b, 0x275c, 0x275d, 0x275e, 0x2764, 0x2794, 0x27a4]),
]

# Old names that keep pointing at their old character
LEGACY = {
    'capital-lambda': 'capital-lamda',
    'small-lambda': 'small-lamda',
    'teta': 'small-theta',
    'carriage_return': 'downwards-arrow-with-corner-leftwards',
    'is-implied-by': 'leftwards-double-arrow',
    'leftright-arrow': 'left-right-arrow',
    'leftright-double-arrow': 'left-right-double-arrow',
    'inverted_exclamation': 'inverted-exclamation-mark',
    'pound_sterling_sign': 'pound-sign',
    'general_currency_sign': 'currency-sign',
    'broken_vertical': 'broken-bar',
    'umlaut': 'diaeresis',
    'ordinal_indicator': ('masculine-ordinal-indicator', 'deprecated: ambiguous name'),
    'angle_quotation': ('right-pointing-double-angle-quotation-mark', 'deprecated: ambiguous name'),
    'plus_or-minus': 'plus-minus-sign',
    'pilcrow_paragraph': 'pilcrow-sign',
    'capital_AE_diphthong': 'capital-ae',
    'multiply_sign': 'multiplication-sign',
    'small_ae_diphthong': 'small-ae',
    'small_o': ('small-o-diaeresis', 'deprecated: ambiguous name'),
    'divide_sign': 'division-sign',
}

out = [
    '// --- ENRON/GLYPH',
    '//',
    '// Escaped characters for use in `content`, e.g. `content: glyph.$copyright-sign`.',
    '// Characters are named after their Unicode name (`$small-e-acute`, `$small-alpha`,',
    '// `$black-star`), every HTML 4 entity is also available under its entity name',
    '// (`$eacute`, `$alpha`, `$hearts`). Entity names are case sensitive: `$Alpha` is Α, `$alpha` is α.',
    '// Some symbols (☀ ⚠ ✔) render as color emoji by default, `font-variant-emoji: text` avoids that.',
    '//',
    '// Generated by scripts/glyph.py, edit that instead.',
]
defined = {}  # normalized name -> codepoint
seen_cp = set()

def define(name, cp, value, comment=''):
    key = name.replace('_', '-')
    if key in defined:
        if defined[key] != cp:
            sys.exit(f'name clash: {name} {hex(defined[key])} {hex(cp)}')
        return
    defined[key] = cp
    out.append(f'${name}: {value};' + (f' // {comment}' if comment else ''))

for title, cps in SECTIONS:
    cps = list(dict.fromkeys(cps))
    out += ['', f'// --- {title}']
    names = {}
    for cp in cps:
        if cp in seen_cp:
            sys.exit(f'codepoint twice: {hex(cp)}')
        seen_cp.add(cp)
        ch = chr(cp)
        name = ASCII_NAMES.get(cp) or uname(cp)
        names[cp] = name
        shown = ch if unicodedata.category(ch)[0] in 'LNPS' else ''
        ent = entities.get(cp)
        define(name, cp, lit(cp), ' '.join(x for x in [shown, f'&{ent};' if ent else ''] if x))
    ents = [(cp, entities[cp]) for cp in cps if cp in entities and entities[cp].replace('_', '-') != names[cp]]
    if ents:
        out += ['', f'// --- {title}: HTML entity names']
        for cp, ent in ents:
            define(ent, cp, f'${names[cp]}')

missing_entities = [hex(c) for c in entities if c not in seen_cp]
if missing_entities:
    sys.exit(f'entities not covered: {missing_entities}')

out += ['', '// --- Aliases and legacy names, kept for compatibility']
for name, target in LEGACY.items():
    note = ''
    if isinstance(target, tuple):
        target, note = target
    cp = defined[target]
    define(name, cp, f'${target}', note)

# Every old name must still exist
gone = [n for n in old if n not in defined]
if gone:
    sys.exit(f'old names missing: {gone}')

print('\n'.join(out))

# Report old names whose character changed
def old_cp(name):
    v = old[name]
    if v.startswith('$'):
        return old_cp(v[1:].replace('_', '-'))
    return int(v.strip('"').lstrip('\\'), 16)
changed = [(n, hex(old_cp(n)), hex(defined[n])) for n in old if old_cp(n) != defined[n]]
print(f'{len(defined)} names, {len(seen_cp)} characters. Changed: {changed}', file=sys.stderr)
