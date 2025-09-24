
```statblock
layout: Basic 5e Layout
name: "Chain-Kraken (Dream Avatar)"
size: Gargantuan
type: Aberration
subtype: Dreamspawn
alignment: chaotic evil
ac: 15
hp: 150 (see Tentacle mechanics)
hit_dice: 20d12+40
speed: swim 50 ft.
stats: [22, 10, 17, 6, 14, 11]
saves:
  - Strength +9
  - Constitution +6
skillsaves:
  - Perception +5
damage_resistances: psychic; bludgeoning, piercing, and slashing from nonmagical attacks
condition_immunities: charmed, frightened, prone
senses: darkvision 120 ft., passive Perception 15
languages: understands Deep Speech but communicates only in psychic whispers
cr: 7
traits:
  - name: "Untouchable Core"
    desc: "The Kraken’s head cannot be damaged directly. The encounter is resolved by destroying its tentacles. The head only withdraws when enough tentacles are destroyed."
  - name: "Tentacle Spawning"
    desc: "At initiative count 20 each round, the Chain-Kraken spawns 1–2 tentacles onto the ship (max 4 active). Tentacles act on the Kraken’s initiative count."
actions:
  - name: "Tentacle (see Tentacle statblock)"
    desc: "Tentacles lash independently. Each tentacle has its own AC, HP, and initiative tied to the Kraken’s."
mechanics:
  - name: "Choking Abyss (Every 3 rounds)"
    desc: "The Kraken begins a psychic chant. Circles of dark water appear on the deck. At the start of the next round, any creature still inside a circle is grappled and restrained by phantom chains until they escape (DC 15 Strength). The effect can be prevented by silencing or distracting the Kraken’s head."
  - name: "Shattermind Screech (Every 4 rounds)"
    desc: "The Kraken charges a psychic blast. At the start of the next round, unless disrupted, all creatures within 40 ft. must succeed on a DC 15 Wisdom saving throw or take 18 (4d8) psychic damage and be incapacitated until the end of their turn."

```
```statblock
layout: Basic 5e Layout
name: "Kraken Tentacle"
size: Large
type: Aberration
subtype: Dreamspawn
alignment: —
ac: 13
hp: 28
hit_dice: 6d10-6
speed: —
stats: [18, 10, 14, 1, 10, 1]
damage_resistances: psychic
condition_immunities: charmed, frightened
senses: blindsight 30 ft.
languages: —
cr: 1
traits:
  - name: "Linked Existence"
    desc: "When a tentacle is destroyed, the Kraken takes 15 psychic damage. When all active tentacles are destroyed, the Kraken retreats beneath the waves and the encounter ends."
actions:
  - name: "Lash"
    desc: "Melee Weapon Attack: +6 to hit, reach 15 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage, and the target must succeed on a DC 14 Strength saving throw or be grappled (escape DC 14)."
  - name: "Crush"
    desc: "Melee Weapon Attack: +6 to hit, one grappled target. Hit: 13 (2d8 + 3) bludgeoning damage and the target is restrained until the grapple ends."

```
