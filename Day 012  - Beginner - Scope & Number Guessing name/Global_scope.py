
#  Global scope

player_health = 10      

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()                   # Namespace
game()
print(player_health) 