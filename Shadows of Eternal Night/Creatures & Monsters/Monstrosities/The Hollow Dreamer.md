
```statblock
layout: Basic 5e Layout
name: "Hollow Dreamer"
size: Large
type: Aberration
alignment: chaotic evil
ac: 15
hp: 140
hit_dice: 16d10+26
speed: 30 ft., hover 30 ft.
stats: [14, 16, 14, 12, 18, 16]
saves:
  - Wis +7
  - Dex +6
skillsaves:
  - Insight +7
  - Perception +7
damage_resistances: psychic; bludgeoning, piercing, slashing from nonmagical attacks
condition_immunities: charmed, frightened, unconscious, prone
senses: darkvision 120 ft., passive Perception 17
languages: telepathy 60 ft.
cr: 7

traits:
  - name: "Hovering"
    desc: "The Hollow Dreamer hovers and does not fall unless forced downward."

  - name: "Phase Shift"
    desc: "When reduced to 70 HP, the Hollow Dreamer immediately triggers its Phase Transition (see encounter notes)."

  - name: "Dream-Form"
    desc: "The Hollow Dreamer can move through other creatures and objects as if they were difficult terrain. It takes 5 psychic damage if it ends its turn inside an object."

actions:
  - name: "Multiattack"
    desc: "The Hollow Dreamer makes two attacks: one Claw and one Psychic Lash."

  - name: "Claw"
    desc: "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4+4) slashing damage."

  - name: "Psychic Lash"
    desc: "Ranged Spell Attack: +7 to hit, range 30 ft., one target. Hit: 14 (3d6+4) psychic damage."

  - name: "Psychic Ripple"
    desc: "One creature the Dreamer can see must make a DC 15 Wisdom saving throw, taking 11 (2d8+2) psychic damage on a failed save, or half as much on a success."

  - name: "Marked Ground"
    desc: "A 10 ft. radius area within 40 ft. erupts with psychic force. Each creature in the area must make a DC 15 Dexterity saving throw, taking 13 (3d6) psychic damage on a failed save, or half as much on a success."

legendary_actions:
  - 2 per turn
  - name: "Nightmare Glare"
    desc: "One creature the Dreamer can see must succeed on a DC 15 Wisdom saving throw or be frightened until the end of its next turn."

  - name: "Shift Along the Ring"
    desc: "The Hollow Dreamer teleports up to 40 feet to another platform segment."

  - name: "Echo Knockback"
    desc: "One creature within 10 ft. must make a DC 15 Dexterity saving throw or take 6 (1d10+1) psychic damage and be pushed 10 ft."

  - name: "Shadow Echo (BA Phase 1 & Phase 2)"
    desc: "Tell (end of turn): A shadowy rune flares beneath two chosen PCs; their silhouette detaches and forms a dormant echo. Resolution (initiative 20): If the echo (AC 12, 5 HP) was not destroyed, it manifests as a hostile Echo Shade (HP 15, simple mimic attack for 5 damage)."

  - name: "Quadrant Mark (BA Phase 2 Only)"
    desc: "Tell (end of turn): One platform quadrant glows with spiraling psychic sigils. Resolution (initiative 20): The marked quadrant erupts. Creatures on that quadrant must make a DC 15 Constitution save, taking 13 (3d6) psychic damage on a fail, or half on a success."

```
