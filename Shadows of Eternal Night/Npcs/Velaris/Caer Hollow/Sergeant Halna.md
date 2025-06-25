title: Sergeant Halna
tags: [npc, caer-hollow, city-guard]

## Overview
Sergeant Halna leads the **City Guard of Caer Hollow**, distinct from the Crownwatch, which answers directly to the capital. Halna is a disciplined, loyal officer with decades of experience keeping order among the city’s common folk. While **Captain Teron Veyne** handles larger-scale Crown matters and strategic defense, Halna is the **boots-on-the-ground authority**, intimately familiar with every street, criminal, and tavern in the city.

## Personality
- **Grizzled, pragmatic**, and no-nonsense
- Fiercely loyal to the people of Caer Hollow
- Wary of politics and mages, but respects effective leadership
- Known for giving second chances — but never third

## Role in the Campaign
- May serve as a **local ally** or point of friction depending on how the party behaves in the city
- She often finds herself cleaning up after Crownwatch decisions or Academy mishaps
- Could be a **valuable contact for street-level rumors**, black market movement, or hidden corners of the city
- If party members break the law, Halna will **show restraint before force**, but she does **not tolerate repeated offenses**

## Appearance
- Stocky build, scarred face, weathered armor with Caer Hollow sigil
- Keeps her greying hair in a tight braid, carries a reinforced baton and crossbow

## Known Associates
- **Teron Veyne** (superior): Professional respect, occasional tension
- Several loyal lieutenants, including **Corwin Brade** (young idealist) and **Thala Murn** (skeptical veteran)

## Possible Hooks
- Can offer **city patrol missions**, lead-ins to smuggling plots, or background on criminal elements
- Might be approached for **off-the-record favors**, or called upon to vouch for the party’s actions to the Crownwatch

```statblock
layout: Basic 5e Layout
name: "Sergeant Halna"
size: Medium
type: humanoid
subtype: human
alignment: lawful neutral
ac: 17 (chain shirt + shield)
hp: 84
hit_dice: 11d8+33
speed: 30 ft.
stats: [16, 12, 14, 10, 14, 13]
saves:
  - Str +5
  - Wis +4
skillsaves:
  - Athletics +5
  - Insight +4
  - Intimidation +4
  - Perception +4
damage_resistances: nonmagical bludgeoning, piercing, slashing (while parrying)
condition_immunities: frightened (while allies are present)
senses: passive Perception 14
languages: Common
cr: 4
traits:
  - name: "Tactical Command"
    desc: "As a bonus action, Halna can shout orders. One allied creature within 30 feet can move up to half its speed or make one weapon attack as a reaction."
  - name: "Disabling Strikes"
    desc: "Halna’s melee attacks are precise and aim to disable. On a hit, the target must succeed on a DC 13 Strength saving throw or be knocked prone or disarmed (Halna’s choice)."
  - name: "Measured Response"
    desc: "When Halna reduces a creature to 0 HP, she can choose to leave them unconscious and stable instead of killing them."
actions:
  - name: "Multiattack"
    desc: "Halna makes two melee attacks with her reinforced baton or one attack and one shove."
  - name: "Reinforced Baton"
    desc: "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) bludgeoning damage and the target must succeed on a DC 13 Constitution saving throw or be stunned until the end of its next turn."
  - name: "Net Toss"
    desc: "Ranged Weapon Attack: +4 to hit, range 5/15 ft., one Medium or smaller creature. Hit: Target is restrained (escape DC 12)."

bonus_actions:
  - name: "Guard's Presence"
    desc: "Once per short rest, Halna can grant herself and up to 2 allies advantage on saving throws against being charmed or frightened until the end of her next turn."

reactions:
  - name: "Shield Interpose"
    desc: "When a creature within 5 feet is targeted by an attack, Halna can impose disadvantage on the roll using her shield."

```
