
```statblock
layout: Basic 5e Layout
name: "The Hollow Dreamer"
size: Large
type: Aberration
alignment: chaotic evil
ac: 15
hp: 140
hit_dice: 16d12+32
speed: 20 ft., hover 30 ft.
stats: [14, 16, 18, 12, 16, 18]
saves:
  - Wis +6
  - Cha +7
skillsaves:
  - Insight +6
  - Deception +7
damage_resistances: psychic; bludgeoning, piercing, slashing (nonmagical)
condition_immunities: charmed, frightened, prone, unconscious
senses: darkvision 120 ft., passive Perception 13
languages: Deep Speech, telepathy 60 ft.
cr: 7

traits:
  - name: "Two-Phase Encounter"
    desc: "Phase 1 from 140–71 hp (intact square). Phase 2 from 70 hp or less (shattered ring). At 14 hp or less, trigger Death Sequence instead of dropping to 0 immediately."

  - name: "Nightmare Form"
    desc: "The Hollow Dreamer can hover over solid ground but cannot enter the central void in Phase 2. It can move freely along the ring."

actions:
  - name: "Multiattack"
    desc: "The Hollow Dreamer makes two attacks: one with Nightmare Lash and one with Claw."

  - name: "Nightmare Lash"
    desc: "Melee Spell Attack: +6 to hit, reach 10 ft., one target. Hit: 10 (2d6 + 3) psychic damage. The target must succeed on a DC 13 Wisdom saving throw or has disadvantage on the next attack roll it makes before the end of its next turn."

  - name: "Claw"
    desc: "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) slashing damage."

  - name: "Psychic Ripple (Recharge 5–6, Phase 1 only)"
    desc: "The Hollow Dreamer unleashes psychic static in a 15-foot cone. Each creature in the area chooses to make a DC 14 Dexterity or Wisdom saving throw. On a failed save, a creature takes 8 (2d6 + 1) psychic damage and is pushed 5 feet away from the Dreamer. On a success, the creature takes half damage and is not pushed."

  - name: "Summon Echo Wisps (Phase 1 only)"
    desc: "The Dreamer summons 1d3 Echo Wisps in unoccupied spaces within 30 feet. Each uses the Shadow stat block with 7 hit points, no Strength Drain feature, and deals 5 (1d6 + 2) psychic damage on a hit. Echo Wisps vanish if they end their turn more than 20 feet from the Dreamer."

  - name: "Marked Ground (Phase 1 only)"
    desc: "The Dreamer marks a 10-foot-radius area on the ground it can see within 60 feet. The area glows faintly until the start of the Dreamer’s next turn. When that turn begins, each creature in the area takes 8 (2d6 + 2) psychic damage. This ability has no saving throw; it is avoided by leaving the area."

  - name: "Reality Tear (Phase 2 only)"
    desc: "The Dreamer tears along the boundary between two quadrants. Each creature in a 30-foot line originating from the Dreamer along a quadrant edge must make a DC 13 Dexterity saving throw, taking 9 (2d6 + 2) force damage on a failed save, or half as much damage on a successful one."

  - name: "Summon Echo Doubles (Phase 2 only)"
    desc: "The Dreamer summons 1 or 2 Echo Doubles in unoccupied spaces in unmarked quadrants within 30 feet. Each Echo Double has AC 12, 12 hit points, speed 30 ft., and one attack: Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) psychic damage. An Echo Double disappears if it ends its turn more than 30 feet from the Dreamer."

  - name: "Pull of the Dreamer (Trigger: Takes 20+ damage in a round, Phase 2 only)"
    desc: "Each creature in the same quadrant as the Dreamer must succeed on a DC 14 Wisdom saving throw or be pulled 5 feet closer to the Dreamer. This movement does not provoke opportunity attacks."

legendary_actions:
  - name: "Quadrant Mark (Phase 2 only)"
    desc: "The Dreamer targets one quadrant of the ring that it can see. That quadrant becomes marked until the start of the Dreamer’s next turn. At the start of its next turn, each creature in the marked quadrant must make a DC 14 Dexterity saving throw, taking 10 (3d6) psychic damage on a failed save, or half as much on a success, and has disadvantage on the next attack roll it makes before the end of its next turn on a failed save. While the Dreamer has 70 hit points or fewer, it instead marks two opposite quadrants."
  - name: "Shift Along the Ring"
    desc: "The Dreamer moves up to half its flying speed to another quadrant along the ring without provoking opportunity attacks."
  - name: "Echo Flare"
    desc: "The Dreamer causes one Echo Wisp or Echo Double within 30 feet to immediately make one attack."

lair_actions:
  - name: "Phase Transition: Shattering (DM Triggered at 70 HP)"
    desc: "When the Dreamer is reduced to 70 hit points or fewer for the first time, the fountain collapses into a central void and the ground fractures into four quadrants forming a ring with 5–8-foot gaps. All terrain becomes difficult until the start of the Dreamer’s next turn. The Dreamer vanishes and reappears at the edge of one quadrant at the end of the round."
  - name: "Phase Transition: Psychic Drag (DM Triggered immediately after Shattering)"
    desc: "At the start of the next round, a psychic pull drags creatures toward the central void. Each creature must succeed on a DC 14 Strength saving throw or be pulled 10 feet toward the center and take 3 (1d4 + 1) psychic damage if they fall. A creature that falls is immediately repositioned to the nearest safe space on a quadrant edge."

reactions:
  - name: "Death Sequence (DM Triggered at 14 HP or less)"
    desc: "Instead of being reduced to 0 hit points, the Dreamer collapses and four spectral tendrils appear, each anchored to a different quadrant. Each tendril has AC 13 and 10 hit points, is resistant to psychic damage, and vulnerable to radiant damage. While at least one tendril remains, the Dreamer cannot be reduced to 0 hit points and regains 5 hit points at the start of each of its turns. When all tendrils are destroyed, a Core Heart appears above the central void: AC 12, 25 hit points, resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks, and vulnerability to radiant damage (each radiant hit deals an additional 5 damage). When the Core Heart is reduced to 0 hit points, the Dreamer is destroyed and the encounter ends."


```
