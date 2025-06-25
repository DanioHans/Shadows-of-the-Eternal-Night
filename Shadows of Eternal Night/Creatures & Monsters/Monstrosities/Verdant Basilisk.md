
```statblock
layout: Basic 5e Layout
name: "Verdant Basilisk"
size: Medium
type: Monstrosity
subtype: Verdant
alignment: unaligned
ac: 15 (natural armor)
hp: 52
hit_dice: 8d8+16
speed: 30 ft.
stats: [16, 8, 15, 2, 8, 7]
saves:
  - Constitution +5
skillsaves:
  - Perception +2
damage_resistances: poison
condition_immunities: poisoned
senses: darkvision 60 ft., passive Perception 12
languages: —
cr: 3
traits:
  - name: "Petrifying Gaze"
    desc: "If a creature starts its turn within 30 feet and the basilisk can see it, the basilisk can force it to make a DC 13 Constitution saving throw. On a failed save, the creature begins to turn to stone and is restrained. It must repeat the save at the end of its next turn. On a second failure, it is petrified for 24 hours. On a success, the effect ends."
  - name: "Toxic Bloom"
    desc: "When the basilisk is first bloodied (below half HP), arcane sap leaks from old scars. The area in a 10-foot radius around it becomes difficult terrain until the end of its next turn as sticky, glowing fluid seeps out. The glow fades quickly, but leaves behind a strange fungal scent."
  - name: "Magic Tainted"
    desc: "Detect Magic reveals a chaotic aura of nature and shadow magic leaking from the creature."
actions:
  - name: "Bite"
    desc: "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage plus 7 (2d6) poison damage."

```