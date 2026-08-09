<p align="center">
  <h1 align="center">VanillaGuide Enhanced</h1>
  <p align="center">
    <strong>The ultimate in-game leveling guide for World of Warcraft 1.12.1 Vanilla</strong>
  </p>
  <p align="center">
    <a href="https://github.com/GabHST/VanillaGuide-Enhanced/releases/tag/v2.0.0"><img src="https://img.shields.io/badge/version-2.0.0-brightgreen" alt="Version"></a>
    <img src="https://img.shields.io/badge/WoW-1.12.1_Vanilla-yellow" alt="WoW">
    <img src="https://img.shields.io/badge/languages-EN_|_PT--BR-blue" alt="Languages">
    <img src="https://img.shields.io/github/downloads/GabHST/VanillaGuide-Enhanced/total?color=purple&label=downloads" alt="Downloads">
    <a href="https://github.com/GabHST/VanillaGuide-Enhanced/stargazers"><img src="https://img.shields.io/github/stars/GabHST/VanillaGuide-Enhanced?style=flat&color=orange" alt="Stars"></a>
  </p>
</p>

---

<p align="center">
  <a href="https://github.com/GabHST/VanillaGuide-Enhanced/releases/download/v2.0.0/VanillaGuide-Enhanced.zip">
    <img src="https://img.shields.io/badge/%E2%AC%87%20Download-English-2ea44f?style=for-the-badge" alt="Download EN">
  </a>
  &nbsp;&nbsp;
  <a href="https://github.com/GabHST/VanillaGuide-Enhanced/releases/download/v2.0.0/VanillaGuide-Enhanced.zip">
    <img src="https://img.shields.io/badge/%E2%AC%87%20Download-Portugu%C3%AAs_(BR)-2ea44f?style=for-the-badge" alt="Download PT-BR">
  </a>
</p>

---

## What is this?

VanillaGuide Enhanced is a **complete rewrite** of the classic VanillaGuide leveling addon. It tells you exactly where to go, what to do, and does most of it automatically.

Works on: **SoloCraft**, Elysium, Kronos, Turtle WoW, or any WoW 1.12.1 server.

---

## Key Features

### GPS Navigation
| Feature | Description |
|---------|-------------|
| **Auto-arrow** | pfQuest arrow automatically points to current step destination |
| **Shift+Click** | Cycle between NPCs, coordinates, and mobs in the step |
| **Distance + ETA** | Shows meters and estimated arrival time |
| **Locked targeting** | Arrow stays on YOUR choice until you change it |
| **Right-click reset** | Click arrow to go back to nearest objective |

### Smart Auto-Quest
| Feature | Description |
|---------|-------------|
| **Auto-accept** | Accepts quests that match the current step (exact name) |
| **Auto-turn-in** | Completes and turns in quests automatically |
| **Multi-quest NPCs** | Handles NPCs with multiple quests correctly |
| **Never wrong** | Will NEVER accept a quest that isn't in the current step |

### Modern UI
| Feature | Description |
|---------|-------------|
| **2-step view** | Current step (bright) + next step (dimmed) |
| **Tips** | Helpful hints below every step in gray |
| **Dark theme** | Clean, modern dark background |
| **Step counter** | `[29/78]` green counter |
| **Combat fade** | Guide fades during combat |

### Guide Quality
| Feature | Description |
|---------|-------------|
| **1 action = 1 step** | Never "do X and Y" in the same step |
| **Exact coords** | All coordinates from pfQuest database |
| **NPC tags** | Every NPC tagged for Shift+Click targeting |
| **Item tags** | Every item tagged for mob resolution via pfDB |

---

## Installation

1. Download the repository ZIP from GitHub (**Code** → **Download ZIP**) or download `VanillaGuide-Enhanced.zip` from the [Releases](https://github.com/GabHST/VanillaGuide-Enhanced/releases) page.
2. Extract the ZIP.
3. Copy the extracted addon folder into your `OctoWoW/Interface/AddOns/` directory.
4. Restart the client or type `/reload`.

Your final folder structure should look like one of these:

```
OctoWoW/Interface/AddOns/VanillaGuide-Enhanced-master/
├── VanillaGuide-Enhanced-master.toc
├── VanillaGuide.lua
├── Core.lua
├── Display.lua
├── UI.lua
├── Settings.lua
├── GuideTables/
└── ...
```

```
OctoWoW/Interface/AddOns/VanillaGuide-Enhanced/
├── VanillaGuide-Enhanced.toc
├── VanillaGuide.lua
├── Core.lua
├── Display.lua
├── UI.lua
├── Settings.lua
├── GuideTables/
└── ...
```

Legacy `VanillaGuide` installs also remain supported.

### Recommended Addons

| Addon | Why |
|-------|-----|
| [pfQuest](https://github.com/shagu/pfQuest) | **GPS arrow** - the guide points pfQuest's arrow to each destination |
| [pfUI](https://github.com/shagu/pfUI) | **Nameplates** - shows quest mob indicators |

---

## Controls

| Input | Action |
|-------|--------|
| `Shift+Click` on step | Cycle targets + point GPS arrow |
| `Right-click` on step | Skip / advance step |
| `Right-click` on arrow | Reset arrow to nearest objective |
| `/vge` | Show all commands |
| `/vge combat` | Toggle combat transparency |
| `/vge skip` | Toggle right-click skip |

---

## Guides Included

### Horde (rewritten with tips + exact coords)
| Zone | Levels | Steps |
|------|--------|-------|
| Deathknell | 1-6 | 44 |
| Tirisfal Glades | 6-10 | 78 |
| Tirisfal Glades | 10-12 | 72 |
| Barrens | 12-15 | 69 |
| Stonetalon Mountains | 15-16 | 12 |
| Barrens (part 1) | 16-20 | 58 |
| Barrens (part 2) | 16-20 | 31 |
| *20-60* | *included* | *original* |

### Alliance
Full 1-60 guides included (original format).

---

## Changelog

### v2.0.0
- Complete rewrite of VG_Enhancements
- pfQuest arrow GPS integration
- Smart auto-quest with exact name matching
- 2-step display with tips
- Modern dark UI
- All Horde guides 1-20 rewritten
- Deferred initialization (no login freeze)

### v1.0
- Initial release

---

## Imported Guides (RestedXP Migration)

Guides from [Slamrish/ModernGuides-Source](https://github.com/Slamrish/ModernGuides-Source) (originally written for the RestedXP addon) have been converted and imported into VanillaGuide-Enhanced's table format under `GuideTables/Alliance/`, `GuideTables/Horde/`, and `GuideTables/Hardcore/`.

### Imported Guide List

| File | Guides | Faction |
|------|--------|---------|
| `011_Human_1to13.lua` | 1-6 Northshire, 6-11 Elwynn Forest, 11-13 Loch Modan | Alliance |
| `010_NightElf_1to10.lua` | 1-6 Shadowglen, 6-11 Teldrassil | Alliance |
| `012_DwarfGnome_1to14.lua` | 1-6 Coldridge Valley, 6-14 Dun Morogh | Alliance |
| `013_NightElf_11to16.lua` | 11-16 Darkshore | Alliance |
| `014_Alliance_11to20.lua` | 11-20 Westfall | Alliance |
| `010_Durotar_1to13.lua` | 1-13 Durotar (Orc/Troll) | Horde |
| `011_Undead_1to13.lua` | 1-13 Tirisfal Glades (Undead) | Horde |
| `012_Mulgore_1to13.lua` | 1-13 Mulgore (Tauren) | Horde |
| `013_Silverpine_13to15.lua` | 13-15 Silverpine Forest | Horde |
| `014_Barrens_15to23.lua` | 15-23 The Barrens | Horde |
| `010_Hardcore_LochModan_18to19.lua` | 18-19 Loch Modan (Hardcore) | Alliance |
| `011_Hardcore_Redridge_19to20.lua` | 19-20 Redridge (Hardcore) | Alliance |
| `012_Hardcore_Imported.lua` | Selected Hardcore guides | Mixed |

### Compatibility Decisions

- **English only**: All imported files include a locale guard (`if GetLocale() ~= "enUS" and GetLocale() ~= "enGB" then return end`). Non-English clients will skip these files silently.
- **RXP shim**: `GuideTables/RXP_Compat.lua` defines no-op stubs for `RXP` and `RXPGuides` globals so any remaining raw references in source files do not cause Lua errors on Classic.
- **Retail APIs removed**: No `C_Timer`, `C_QuestLog`, or other Retail-only APIs are used. All guide content is purely declarative text in VanillaGuide table format.
- **Class-specific steps**: Steps gated to a specific class (e.g., Warlock, Rogue) are included with a `(ClassName only)` suffix in the step text. Negation gates (`!Warrior`) are treated as universal and shown without annotation.
- **Multi-waypoint routes**: RXP `.goto` waypoints are collapsed to the final destination only; intermediate waypoints are omitted.
- **Video/link references**: External video links from `.link` directives are omitted (URLs cannot be opened in-game on Classic). The step text retains any accompanying description.

### Manual Follow-Ups

- Coordinate accuracy: RXP coordinates use the RXP map system. Some coordinates may be slightly off for vanilla zone layouts — spot-check in-game and adjust `x`/`y` values in the relevant `GuideTables/` file as needed.
- The `Hardcore.lua` source (1.9 MB) was only partially imported (first 10 guides). Additional Hardcore guides can be converted by re-running `/tmp/convert_guides.py` against the full source file.
- Quest IDs referenced in step text (from `.accept`/`.turnin` >> text) are display-only and have no runtime effect in VanillaGuide.

---

## Credits

- Original VanillaGuide by **mrmr** and **lanjelin**
- Enhanced by **GabHST**
- RestedXP guide content by **RestedXP team** (imported with Classic-compat conversion)

## License

MIT

---

## Auto-Update

This addon supports **silent auto-update** via `LaunchSoloCraft.ps1`. Every time you launch WoW through the launcher:

1. It checks the latest release on GitHub
2. Compares with your installed version
3. Downloads and installs automatically if outdated
4. Shows a notification in WoW chat when loaded

No manual download needed after first install!
