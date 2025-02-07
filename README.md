# Defeat_the_EvilWiz
Welcome to Defeat The Evil Wizard, a text-based RPG game where you engage in turn-based combat against a powerful Evil Wizard.

Defeat the Evil Wizard to unlock the White Wizard, a powerful sorcerer who can summon minions in battle!
Each character has unique abilities, and you'll need to use strategy to win.
Features:
 Choose from 4 Playable Characters (Warrior, Mage, Archer, Paladin).
 Turn-based Battle System with attacks, healing, and special abilities.
 The Evil Wizard can regenerate and summon minions for a powerful attack.
 Unlock the White Wizard upon victory, with exclusive abilities.
 Minion Summoning Ability (One-time use per battle, deals 30 damage).
 Replayable Game Loop – Play again with the new character after winning!
 Game Mechanics:
1. Character Selection
When you start the game, you'll be prompted to choose your character class:

🛡 Warrior – High health, decent attack power, Power Slash: Deals 30 damage (can only be used once per battle), Battle Cry: Increases attack power by 5.
🔥 Mage – Strong attacks, but lower health, Fireball: (80% chance to hit) deals 40 damage, Arcane Barrier: Blocks the next attack.
🏹 Archer – Balanced character with moderate stats, Quick Shot: Fires two arrows in one turn, Evade: Dodges the next attack..
✨ Paladin – Lower attack power but good survivability, Holy Strike: Deals an extra 15 damage (can only be used once per battle), Divine Shield: Blocks the next attack..
🧙‍♂️ White Wizard (Unlockable) – Has highest health, highest attack power, summons divine light, Purification: Reduces enemy attack power by 10 and prevents healing.

2. Combat System
The battle is turn-based. Each turn, you can:

1 Attack – Deal randomized damage based on your character’s attack power.
2 Special Attack - Uses a specal ability
3 Heal – Restore 20 HP (can’t attack the same turn).
4 View Stats – Check your current health and attack power.
5 (White Wizard Only) Summon Divine Light - Deal 30 damage instantly (one-time use).

1. Evil Wizard’s Abilities
Regeneration – Gains 10 HP per turn.
Summon Minions (One-time use) – Minions attack for 30 damage!
Dark Curse - Reduces player attack power by 5 (used if below 40 health).
Normal Attack – Randomized damage each turn.
2. How to Unlock the White Wizard
Defeat the Evil Wizard once.
Restart the game, and the White Wizard becomes a playable character!
White Wizard has the same powers as the Evil Wizard.

Code Structure:
Character Class: Base class for all characters.
Subclasses (Warrior, Mage, Archer, Paladin, WhiteWizard, EvilWizard): Define unique abilities.
create_character Function: Handles player class selection.
battle Function: Manages combat mechanics and turns.
main Function: Handles game flow, victory conditions, and replay options.

Game Flow:
The player selects a character.
The player names the character.
The battle begins with turn-based choices.
The Evil Wizard responds with attacks, healing, or debuffs.
The game continues until one character's health reaches zero.
If the player wins, they unlock the White Wizard for future battles.
The player can choose to play again or exit.

Example Gameplay:
Choose your character class:
1. Warrior
2. Mage
3. Archer
4. Paladin
Enter the number of your class choice: 1
Enter your character's name: Aragon

--- Battle Begins! ---

Your Turn:
1. Attack
2. Heal
3. View Stats
Choose an action: 1
Aragon attacks The Dark Wizard for 22 damage!

The Dark Wizard regenerates 5 health!
The Dark Wizard attacks Aragon for 15 damage!

Your Turn:
1. Attack
2. Heal
3. View Stats
Choose an action: 2
Aragon heals for 10 HP! Current health: 125

The Dark Wizard summons dark minions! They deal 30 damage!

