
```statblock
layout: Basic 5e Layout
name: "Arcane Resonance Elemental"
size: Medium
type: Elemental
subtype: Arcane Construct
alignment: unaligned
ac: 13
hp: 68
hit_dice: 8d8+24
speed: 30 ft., fly 30 ft. (hover)
stats: [14, 12, 16, 6, 12, 8]
damage_resistances: acid, cold, fire, lightning, thunder; bludgeoning, piercing, slashing from nonmagical attacks
damage_immunities: force
condition_immunities: charmed, frightened, grappled, paralyzed, petrified, prone
senses: darkvision 60 ft., passive Perception 11
languages: —
cr: 3
traits:
  - name: "Arcane Instability"
    desc: "At the start of each of the elemental’s turns, roll a d4 to determine the damage type its attacks deal that round: 1—fire, 2—lightning, 3—cold, 4—force."
  - name: "Spell Disruption"
    desc: "Whenever a creature casts a spell within 10 feet of the elemental, that creature must succeed on a DC 13 Constitution saving throw or take 5 (1d10) force damage as arcane feedback lashes out."
actions:
  - name: "Resonance Slam"
    desc: "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) damage of the elemental’s current Arcane Instability type."
  - name: "Arcane Pulse (Recharge 5–6)"
    desc: "The elemental releases a burst of unstable magical energy in a 15-foot radius. Creatures in the area must make a DC 13 Dexterity saving throw, taking 14 (4d6) force damage on a failed save, or half as much damage on a successful one."
  - name: "Unstable Collapse"
    desc: "When the Arcane Resonance Elemental is reduced to 0 hit points, it explodes in arcane backlash. Creatures within 10 ft. must make a DC 13 Dexterity saving throw, taking 10 (3d6) force damage on a failed save, or half as much on a success."
```
