#Leon Kobia
#20/2/26
class FighterCharacter:

    def __init__(self, role, health, damage, speed):
        self.character_role = role
        self.character_health = health
        self.character_damage = damage
        self.character_speed = speed

    def run(self, direction):
        print(f"Game log: {self.character_role} runs {direction} at speed {self.character_speed}")

    def report_status(self):
        print(f"\nCharacter Log: \nRole: {self.character_role} \nHealth: {self.character_health} "
              f"\nDamage: {self.character_damage} \nSpeed: {self.character_speed}\n___\n")

    def kick(self, opponent):
        # Corrected: subtract damage from opponent's health
        character_damage = self.character_damage
        opponent.character_health -= character_damage
        # Prevent negative health
        opponent.character_health = max(0, opponent.character_health)
        print(f"Game Log: {self.character_role} deals a damage of {character_damage} to the {opponent.character_role}.")

    def takle(self, opponent):
        # Adventurous: subtract damage from opponent's speed
        character_damage = self.character_damage
        opponent.character_speed -= character_damage
        # Prevent negative speed
        opponent.character_speed = max(0, opponent.character_speed)
        print(f"Game Log: {self.character_role} tackles {opponent.character_role} and reduces their speed by {character_damage}.")


# Create characters
ninja_character = FighterCharacter("Ninja", health=100, damage=40, speed=120)
warrior_character = FighterCharacter("Warrior", health=160, damage=80, speed=80)

# Initial status
ninja_character.report_status()
warrior_character.report_status()

# Actions
ninja_character.run("Up")
ninja_character.kick(warrior_character)

# Status after kick
ninja_character.report_status()
warrior_character.report_status()

# Extra credit: tackle
warrior_character.takle(ninja_character)

# Status after tackle
ninja_character.report_status()
warrior_character.report_status()
