import json
import os
import re
import shutil
import urllib.parse
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
WORK = REPO / 'rxp_work'
SOURCE_DIR = WORK / 'source_guides'
OUTPUT_DIR = WORK / 'generated'
BASE_URL = 'https://raw.githubusercontent.com/Slamrish/ModernGuides-Source/main/'
START_KEY = 1000  # Reserved range for imported RXP guides.

FILE_SPECS = [
    {
        'source': 'A-Classic-Alliance-1-10_NightElf.lua',
        'output_subdir': 'Alliance',
        'output_filename': '010_NightElf_1to10.lua',
        'table_name': 'Table_010_RXP_NightElf_1to10',
        'menu_group': 'Alliance (RXP)',
    },
    {
        'source': 'A-Classic-Alliance-1-13_Human.lua',
        'output_subdir': 'Alliance',
        'output_filename': '011_Human_1to13.lua',
        'table_name': 'Table_011_RXP_Human_1to13',
        'menu_group': 'Alliance (RXP)',
    },
    {
        'source': 'A-Classic-Alliance-1-14_DwarfGnome.lua',
        'output_subdir': 'Alliance',
        'output_filename': '012_DwarfGnome_1to14.lua',
        'table_name': 'Table_012_RXP_DwarfGnome_1to14',
        'menu_group': 'Alliance (RXP)',
    },
    {
        'source': 'A-Classic-Alliance-11-16_NightElf.lua',
        'output_subdir': 'Alliance',
        'output_filename': '013_NightElf_11to16.lua',
        'table_name': 'Table_013_RXP_NightElf_11to16',
        'menu_group': 'Alliance (RXP)',
    },
    {
        'source': 'A-Classic-Alliance-11-20.lua',
        'output_subdir': 'Alliance',
        'output_filename': '014_Alliance_11to20.lua',
        'table_name': 'Table_014_RXP_Alliance_11to20',
        'menu_group': 'Alliance (RXP)',
    },
    {
        'source': 'H-Classic-Horde-01-13_Durotar.lua',
        'output_subdir': 'Horde',
        'output_filename': '010_Durotar_1to13.lua',
        'table_name': 'Table_010_RXP_Durotar_1to13',
        'menu_group': 'Horde (RXP)',
    },
    {
        'source': 'H-Classic-Horde-01-13_Undead.lua',
        'output_subdir': 'Horde',
        'output_filename': '011_Undead_1to13.lua',
        'table_name': 'Table_011_RXP_Undead_1to13',
        'menu_group': 'Horde (RXP)',
    },
    {
        'source': 'H-Classic-Horde-1-13_Mulgore.lua',
        'output_subdir': 'Horde',
        'output_filename': '012_Mulgore_1to13.lua',
        'table_name': 'Table_012_RXP_Mulgore_1to13',
        'menu_group': 'Horde (RXP)',
    },
    {
        'source': 'H-Classic-Horde-13-15_Silverpine.lua',
        'output_subdir': 'Horde',
        'output_filename': '013_Silverpine_13to15.lua',
        'table_name': 'Table_013_RXP_Silverpine_13to15',
        'menu_group': 'Horde (RXP)',
    },
    {
        'source': 'H-Classic-Horde-15-23_Barrens.lua',
        'output_subdir': 'Horde',
        'output_filename': '014_Barrens_15to23.lua',
        'table_name': 'Table_014_RXP_Barrens_15to23',
        'menu_group': 'Horde (RXP)',
    },
    {
        'source': 'A-Hardcore-18-19 Loch Modan.lua',
        'output_subdir': 'Hardcore',
        'output_filename': '010_Hardcore_LochModan_18to19.lua',
        'table_name': 'Table_010_RXP_Hardcore_LochModan_18to19',
        'menu_group': 'Hardcore (RXP)',
    },
    {
        'source': 'A-Hardcore-19-20 Redridge.lua',
        'output_subdir': 'Hardcore',
        'output_filename': '011_Hardcore_Redridge_19to20.lua',
        'table_name': 'Table_011_RXP_Hardcore_Redridge_19to20',
        'menu_group': 'Hardcore (RXP)',
    },
    {
        'source': 'Hardcore.lua',
        'output_subdir': 'Hardcore',
        'output_filename': '012_Hardcore_Imported.lua',
        'table_name': 'Table_012_RXP_Hardcore_Imported',
        'menu_group': 'Hardcore (RXP)',
        'limit_guides': 8,
    },
]

KNOWN_CLASSES = {
    'Druid', 'Hunter', 'Mage', 'Paladin', 'Priest', 'Rogue', 'Shaman',
    'Warlock', 'Warrior'
}

IGNORE_PREFIXES = (
    '#sticky', '#label', '#requires', '#completewith', '#loop', '#era',
    '#som', '#era/som', '#season', '#hardcore', '#classic', '#tbc', '#group',
    '#subgroup', '#defaultfor', '#next', '#name', '#version', '#author',
    '#softcore', '#phase'
)

ZONE_ALIASES = {
    '1414': 'Kalimdor',
    '1415': 'Eastern Kingdoms',
    '1429': 'Elwynn Forest',
    '1436': 'Westfall',
    '1439': 'Darkshore',
    'StormwindClassic': 'Stormwind City',
}


def download_sources():
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    for spec in FILE_SPECS:
        src = spec['source']
        dest = SOURCE_DIR / src
        url = BASE_URL + urllib.parse.quote(src)
        with urllib.request.urlopen(url) as response:
            dest.write_bytes(response.read())


def sanitize_text(text: str) -> str:
    text = text.strip()
    text = re.sub(r'\s+--.*$', '', text)
    text = re.sub(r'\s*<<.*$', '', text)
    text = re.sub(r'\|T[^|]+\|t', '', text)
    text = re.sub(r'\|c[0-9A-Fa-f]{8}', '', text)
    text = re.sub(r'\|cRXP_[A-Za-z_]+_', '', text)
    text = text.replace('|r', '')
    text = text.replace('|', '')
    text = re.sub(r'\[(.*?)\]', r'\1', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = text.replace(' ,', ',')
    text = text.replace(' .', '.')
    return text


def strip_leading(text: str, prefixes) -> str:
    for prefix in prefixes:
        if text.lower().startswith(prefix.lower()):
            return text[len(prefix):].strip()
    return text


def lua_string(text: str) -> str:
    text = text.replace('\\', '\\\\').replace('"', '\\"')
    return f'"{text}"'


def prettify_defaultfor(value: str) -> str:
    value = value.replace('/', ' / ')
    value = re.sub(r'([a-z])([A-Z])', r'\1 \2', value)
    value = re.sub(r'\s+', ' ', value)
    return value.strip()


def title_with_default(meta: dict) -> str:
    title = meta.get('name', 'Imported RXP Guide').strip()
    defaultfor = meta.get('defaultfor')
    if defaultfor:
        pretty = prettify_defaultfor(defaultfor)
        if pretty and pretty.lower() not in title.lower():
            title = f'{title} ({pretty})'
    return title


def normalize_zone(zone: str) -> str:
    zone = sanitize_text(zone)
    return ZONE_ALIASES.get(zone, zone)


def parse_single_guide(text: str):
    lines = text.strip().splitlines()
    meta = {}
    steps = []
    current_step = None
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        if line.startswith('#name '):
            meta['name'] = line[6:].strip()
            continue
        if line.startswith('#group '):
            meta['group'] = line[7:].strip()
            continue
        if line.startswith('#subgroup '):
            meta['subgroup'] = line[10:].strip()
            continue
        if line.startswith('#defaultfor '):
            meta['defaultfor'] = line[12:].strip()
            continue
        if line.startswith('#next '):
            meta['next'] = line[6:].strip()
            continue
        if line.startswith('step') or line == 'ste':
            if current_step is not None:
                steps.append(current_step)
            class_filter = None
            if '<<' in line:
                class_filter = line.split('<<', 1)[1].strip()
            current_step = {'lines': [], 'class_filter': class_filter}
            continue
        if current_step is not None:
            current_step['lines'].append(line)
    if current_step is not None:
        steps.append(current_step)
    return meta, steps


def parse_rxp_guides(content: str):
    pattern = r'RXPGuides\.RegisterGuide\(\[\[(.+?)\]\]\)'
    guides = []
    for match in re.finditer(pattern, content, re.DOTALL):
        guides.append(parse_single_guide(match.group(1)))
    return guides


def directive_with_text(line: str, keyword: str):
    m = re.match(rf'\.{keyword}\b.*?>>\s*(.+)', line)
    return sanitize_text(m.group(1)) if m else None


def maybe_add_sentence(parts, text, prefix=None):
    text = sanitize_text(text)
    if not text:
        return
    if prefix:
        text = f'{prefix}{text}'
    if text not in parts:
        parts.append(text)


def convert_step_to_item(step, guide_defaultfor=None):
    parts = []
    goto_coord = None
    goto_zone = None
    class_filter = step.get('class_filter')
    map_override = None

    for raw in step['lines']:
        line = raw.strip()
        if not line:
            continue
        if line.startswith('--'):
            continue
        if line.startswith('#map '):
            map_override = normalize_zone(line[5:].strip())
            continue
        if any(line.startswith(prefix) for prefix in IGNORE_PREFIXES):
            continue

        m = re.match(r'\.goto\s+([^,]+),\s*(-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)', line)
        if m:
            zone = map_override or normalize_zone(m.group(1))
            x = round(float(m.group(2)))
            y = round(float(m.group(3)))
            if goto_coord is None:
                goto_coord = (x, y)
                goto_zone = zone
            parts.append(f'Go to #COORD[{x},{y}]# in {zone}.')
            continue

        m = re.match(r'\.accept\s+[\d,]+\s*>>\s*(.+)', line)
        if m:
            text = strip_leading(sanitize_text(m.group(1)), ('Accept ',))
            parts.append(f'Accept #GET{text}#.')
            continue

        m = re.match(r'\.turnin\s+[\d,]+\s*>>\s*(.+)', line)
        if m:
            text = strip_leading(sanitize_text(m.group(1)), ('Turn in ', 'Turnin '))
            parts.append(f'Turn in #IN{text}#.')
            continue

        m = re.match(r'\.complete\s+[\d,]+\s*--\s*(.+)', line)
        if m:
            text = strip_leading(sanitize_text(m.group(1)), ('Collect ',))
            parts.append(f'#DO{text}#.')
            continue

        m = re.match(r'\.xp\s+([^\s]+)(?:\s*>>\s*(.+))?$', line)
        if m:
            if m.group(2):
                maybe_add_sentence(parts, m.group(2))
            else:
                target = sanitize_text(m.group(1))
                if '-' in target:
                    parts.append(f'Grind until {target}.')
                else:
                    parts.append(f'Grind to level {target}.')
            continue

        m = re.match(r'\.target\s+\+?(.+)', line)
        if m:
            parts.append(f'Target #NPC{sanitize_text(m.group(1))}#.')
            continue

        m = re.match(r'\.mob\s+\+?(.+)', line)
        if m:
            parts.append(f'Kill #NPC{sanitize_text(m.group(1))}#.')
            continue

        m = re.match(r'\.collect\s+[^-]+--\s*(.+)', line)
        if m:
            text = strip_leading(sanitize_text(m.group(1)), ('Collect ',))
            parts.append(f'Collect #ITEM{text}#.')
            continue

        m = re.match(r'\.use\s+\d+\s*>>\s*(.+)', line)
        if m:
            maybe_add_sentence(parts, m.group(1))
            continue

        m = re.match(r'\.hs\s*>>\s*(.+)', line)
        if m:
            maybe_add_sentence(parts, m.group(1))
            continue
        if line == '.hs':
            parts.append('Hearth to your Inn.')
            continue

        m = re.match(r'\.zone\s+[^>]+>>\s*(.+)', line)
        if m:
            maybe_add_sentence(parts, m.group(1))
            continue

        m = re.match(r'\.home\b.*?>>\s*(.+)', line)
        if m:
            maybe_add_sentence(parts, m.group(1))
            continue

        m = re.match(r'\.fly\b.*?>>\s*(.+)', line)
        if m:
            maybe_add_sentence(parts, m.group(1))
            continue

        m = re.match(r'\.fp\b.*?>>\s*(.+)', line)
        if m:
            maybe_add_sentence(parts, m.group(1))
            continue

        m = re.match(r'\.vendor\b.*?>>\s*(.+)', line)
        if m:
            maybe_add_sentence(parts, m.group(1))
            continue

        m = re.match(r'\.train\b.*?>>\s*(.+)', line)
        if m:
            maybe_add_sentence(parts, m.group(1))
            continue

        m = re.match(r'\.link\s+\S+\s*>>\s*(.+)', line)
        if m:
            parts.append(f'#VIDEO{sanitize_text(m.group(1))}#.')
            continue

        generic = re.match(r'\.[A-Za-z_]+\b.*?>>\s*(.+)', line)
        if generic:
            maybe_add_sentence(parts, generic.group(1))
            continue

        if line.startswith('>>'):
            maybe_add_sentence(parts, line[2:].strip())
            continue

        if line.startswith('+'):
            maybe_add_sentence(parts, line[1:].strip())
            continue

        if line.startswith('.'):
            continue

        maybe_add_sentence(parts, line)

    if not parts:
        return None

    text = ' '.join(parts)
    text = re.sub(r'\s+', ' ', text).strip()
    if re.fullmatch(r'#[A-Za-z0-9_-]+', text):
        return None

    if class_filter:
        tokens = [t for t in class_filter.split() if t]
        if any(t.startswith('!') for t in tokens):
            return None
        if len(tokens) == 1:
            label = tokens[0]
            suffix = 'only'
            if label in KNOWN_CLASSES:
                text = f'{text} ({label} {suffix})'
            else:
                text = f'{text} ({prettify_defaultfor(label)} {suffix})'
        else:
            return None

    item = {'str': text}
    if goto_coord and goto_zone:
        item['x'] = goto_coord[0]
        item['y'] = goto_coord[1]
        item['zone'] = goto_zone
    return item


def render_table(table_name, entries):
    lines = [
        '-- Imported from Slamrish/ModernGuides-Source (RXP format)',
        '-- Classic-compatible conversion for VanillaGuide-Enhanced',
        '-- English only',
        '',
        'if GetLocale() ~= "enUS" and GetLocale() ~= "enGB" then return end',
        '',
        f'{table_name} = {{'
    ]
    for entry in entries:
        lines.append(f'    [{entry["key"]:04d}] = {{')
        lines.append(f'        title = {lua_string(entry["title"])},')
        lines.append('        items = {')
        for idx, item in enumerate(entry['items'], start=1):
            suffix = []
            if 'x' in item:
                suffix.append(f'x = {item["x"]}')
                suffix.append(f'y = {item["y"]}')
                suffix.append(f'zone = {lua_string(item["zone"])}')
            extra = ''
            if suffix:
                extra = ', ' + ', '.join(suffix)
            lines.append(f'            [{idx}] = {{ str = {lua_string(item["str"])}{extra} }},')
        lines.append('        }')
        lines.append('    },')
    lines.append('}')
    lines.append('')
    return '\n'.join(lines)


def main():
    download_sources()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest = []
    next_key = START_KEY

    for spec in FILE_SPECS:
        content = (SOURCE_DIR / spec['source']).read_text(encoding='utf-8')
        guides = parse_rxp_guides(content)
        if spec.get('limit_guides'):
            guides = guides[: spec['limit_guides']]
        entries = []
        for meta, steps in guides:
            title = title_with_default(meta)
            items = [{'str': title}]
            for step in steps:
                item = convert_step_to_item(step, meta.get('defaultfor'))
                if item:
                    items.append(item)
            entries.append({'key': next_key, 'title': title, 'items': items})
            next_key += 1
        out_dir = OUTPUT_DIR / spec['output_subdir']
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / spec['output_filename']
        out_path.write_text(render_table(spec['table_name'], entries), encoding='utf-8')
        manifest.append({
            'source': spec['source'],
            'output_subdir': spec['output_subdir'],
            'output_filename': spec['output_filename'],
            'table_name': spec['table_name'],
            'menu_group': spec['menu_group'],
            'titles': [entry['title'] for entry in entries],
            'keys': [entry['key'] for entry in entries],
            'guide_count': len(entries),
        })

    (OUTPUT_DIR / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')

if __name__ == '__main__':
    main()
