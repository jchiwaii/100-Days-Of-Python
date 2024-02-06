enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies() # Prints the number 2 
print(f"enemies outside function: {enemies}") # Prints the number 1

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength) # Nothing is printed, out of scope

drink_potion() # Number 2 is printed 
print(potion_strength) # Error, defined outside local scope

# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion() # Prints the number 2

print(player_health) # Prints 10

# There is no Block Scope

game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# Modifying Global Scope

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

