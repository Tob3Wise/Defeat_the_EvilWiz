import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        self.can_attack = True  # Player exchanges attack for healing
        self.block_next_attack = False  # Used for defensive abilities
    
    
    def attack(self, opponent):
        if self.can_attack:
            damage_dealt = random.randint(self.attack_power - 10, self.attack_power + 5)  # Randomized damage
            opponent.health -= damage_dealt
            print(f"{self.name} attacks {opponent.name} for {damage_dealt} damage!")
        else:
            print(f'{self.name} cannot attack this turn!')
            self.can_attack = True  # Reset attack availability

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def take_damage(self, damage):
        if self.block_next_attack:
            print(f"{self.name} blocks the attack!")
            self.block_next_attack = False  # Reset after blocking
        else:
            self.health -= damage
            if self.health <= 0:
                print(f"{self.name} has been defeated!")        

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Character healing method
    def healing_potion(self):
        heal_amount = 20
        if self.health < self.max_health:
            self.health = min(self.health + heal_amount, self.max_health)  # Prevent exceeding max health
            self.can_attack = False
            print(f'{self.name} heals for {heal_amount} HP! Current health: {self.health}')
        else:
            print(f'{self.name} is already at full health!')


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.slash_used = False

    def power_slash(self, opponent):
        if not self.slash_used:
             print(f"{self.name} uses Power Slash! Deals 30 damage!")
             opponent.take_damage(30)
        else:
            self.slash_used = True
            print(f'{self.name} has no more energy to Power Slash')

    def battle_cry(self):
        self.attack_power += 5
        print(f"{self.name} uses Battle Cry! Attack power increased to {self.attack_power}!")    

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def fireball(self, opponent):
        if random.random() < 0.8:  # 80% chance to hit
            print(f"{self.name} casts Fireball! Deals 40 damage!")
            opponent.take_damage(40)
        else:
            print(f"{self.name}'s Fireball missed!")

    def arcane_barrier(self):
        print(f"{self.name} activates Arcane Barrier to block attack!")
        self.block_next_attack = True    

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)

    def quick_shot(self, opponent):
        print(f"{self.name} uses Quick Shot! Fires two arrows!")
        self.attack(opponent)
        self.attack(opponent)

    def evade(self):
        print(f"{self.name} dodges the next attack!")
        self.block_next_attack = True      

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15)
        self.strike_used = False

    def holy_strike(self, opponent):
        if not self.strike_used:
            print(f"{self.name} uses Holy Strike! Deals extra 15 damage!")
            opponent.take_damage(self.attack_power + 15)
        else:
            print(f'{self.name} has already used Holy Strike')

    def divine_shield(self):
        print(f"{self.name} activates Divine Shield! Blocks the next attack.")
        self.block_next_attack = True      

# Evil Wizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
        self.summon_used = False  # Special attack can only be used once

    # Evil Wizard's special ability: Regeneration
    def regenerate(self):
        heal_amount = 10
        self.health = min(self.health + heal_amount, self.max_health)  # Prevent exceeding max health
        print(f"{self.name} regenerates {heal_amount} health! Current health: {self.health}")

    # Special Attack: Summon Minions (can only be used once)
    def summon_minions(self, opponent):
        if not self.summon_used:
            print(f"{self.name} summons dark minions! They deal 30 damage!")
            opponent.health -= 30
            self.summon_used = True  # Can only be used once
        else:
            print(f"{self.name} has already used the minion summon!")
                  
    def dark_curse(self, opponent):
        opponent.attack_power -= 5
        print(f"{self.name} casts Dark Curse! {opponent.name}'s attack power reduced to {opponent.attack_power}!")


# Unlockable White Wizard 
class WhiteWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=180, attack_power=30)
        self.name = "White Wizard"  # Default name
        self.summon_light = False

 # Special Attack: Summon Divine Light (can only be used once)
    def summon_divine_light(self, opponent):
        if not self.summon_light:
            print(f"{self.name} summons divine light! They deal 30 damage!")
            opponent.health -= 30
            self.summon_light = True  # Can only be used once
        else:
            print(f"{self.name} has already used divine light!")

    def purification(self, opponent):
        opponent.attack_power -= 10
        print(f"{self.name} uses Purification! {opponent.name}'s attack power weakened.")
        print(f"{opponent.name} can no longer heal this turn.")        


# Function to create player character based on user input
def create_character(unlocked_white_wizard=False):
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  
    print("4. Paladin")  
    if unlocked_white_wizard:
        print("5. White Wizard (Unlocked)")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    elif class_choice == '5' and unlocked_white_wizard:
        return WhiteWizard(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Special Ability")
        print("3. Heal")
        print("4. View Stats")
        if isinstance(player, WhiteWizard):  # White Wizard gets special option
            print("5. Summon Divine Light")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Archer):
                player.quick_shot(wizard)
            elif isinstance(player, Paladin):
                player.holy_strike(wizard)
            elif isinstance(player, Mage):
                player.fireball(wizard)
            elif isinstance(player, Warrior):
                player.power_slash(wizard)
            elif isinstance(player, WhiteWizard):
                player.purification(wizard)
        elif choice == '3':       
            player.healing_potion()    
        elif choice == '4':
            player.display_stats()
        elif choice == '5' and isinstance(player, WhiteWizard):  # White Wizard uses special attack
            player.summon_divine_light(player)
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn
        if wizard.health > 0:
            if not wizard.summon_used:
                wizard.summon_minions(player)  # Evil Wizard summons minions once
            else:
                 wizard.regenerate()
                 wizard.attack(player) or wizard.dark_curse(player)
                
        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            return False  # Player lost

    if wizard.health <= 0:
        print(f"The {wizard.name} has been defeated by {player.name}!")
        return True  # Player won

# Main function to handle the flow of the game
def main():
    unlocked_white_wizard = False  # Track if White Wizard is unlocked
    
    while True:
        # Character creation phase
        player = create_character(unlocked_white_wizard)

        # Evil Wizard is created
        wizard = EvilWizard("The Dark Wizard")

        # Start the battle
        player_won = battle(player, wizard)

        if player_won:
            unlocked_white_wizard = True  # Unlock White Wizard after victory
            print('Congratulations! You have unlocked the White Wizard')

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
