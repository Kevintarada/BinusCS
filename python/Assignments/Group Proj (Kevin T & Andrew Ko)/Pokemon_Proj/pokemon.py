import random
from Pokemon_Proj.pokemon_battle_class import YourPokemon
from Pokemon_Proj.pokemon_general_class import Pokemon

player_info = {}
player_location = [0, 0]
Your_pokemon = [YourPokemon("Pikachu", 5, "thunder", "Female", 8000, 0, 2000),
                YourPokemon("Bulbasaur", 5, "grass", "Male", 6000, 0, 2800),
                YourPokemon("Squirtle", 5, "water", "Female", 7000, 0, 2050),
                YourPokemon("Charmander", 5, "fire", "Male", 9000, 0, 3000)]

def input_player(player_info):
    player_name = input("Your name: ").title()
    player_info ["Name"] = player_name
    player_age = int(input("Age: "))
    player_info ["Age"] = player_age
    player_gender = input("Gender: ").title()
    player_info ["Gender"] = player_gender

def verify():
    question=input("Are these info(s) correct?\n1. Yes\n2. No\n")
    if question == "1":
        print("Hi {}".format(player_info["Name"]))
        print("#You're given 4 pokemon")
        print("#You are in a 10x10 grid")
        print("#You can move one grid to the direction you insert and pokemon will appear randomly which you'll battle")
        move_player(player_location)

    elif question == "2":
        input_player(player_info)
        verify()

    else:
        print("Choose from the list!")
        verify()

def main():
    ans = input("Pokemon simulator..\n1. Play\n2. Exit\nChoice: ")
    if ans == "1":
        input_player(player_info)
        print("Player info:")
        for i in player_info.keys():
            values = player_info[i]
            print("{} = {}".format(i, values))
        verify()

    elif ans == "2":
        print("Bye~")

    else:
        print("Choose from list...")
        main()


def move_player(player_location):
    while True:
        print("(up=u, left=l, right=r, down=d)")
        direction = input("Direction: ")
        add_location(player_location, direction)


def add_location(player_location, direction):
    if direction == "u":
        check_location(player_location, direction)
        player_location[1] = player_location[1]+1
        print(player_location)
        meet_pokemon_location(player_location)

    elif direction == "d":
        check_location(player_location, direction)
        player_location[1] = player_location[1]-1
        print(player_location)
        meet_pokemon_location(player_location)

    elif direction == "l":
        check_location(player_location, direction)
        player_location[0]=player_location[0]-1
        print(player_location)
        meet_pokemon_location(player_location)

    elif direction == "r":
        check_location(player_location, direction)
        player_location[0] = player_location[0]+1
        print(player_location)
        meet_pokemon_location(player_location)

    else:
        print("Choose from option!")
        move_player(player_location)


def check_location(player_location, direction):
    if direction == "u":
        if (player_location[1]+1) > 5:
            print("End of map, choose another direction")
            move_player(player_location)

        else:
            return player_location

    elif direction == "d":
        if player_location[1]-1 < -5:
            print("End of map, choose another direction")
            move_player(player_location)

        else:
            return player_location

    elif direction == "l":
        if player_location[0]-1 < -5:
            print("End of map, choose another direction")
            move_player(player_location)

        else:
            return player_location

    elif direction == "r":
        if player_location[0]+1 > 5:
            print("End of map, choose another direction")
            move_player(player_location)

        else:
            return player_location


def meet_pokemon_location(player_location):
    enemy_chance = random.randint(0,100)
    if enemy_chance >= 85:
        the_enemy = enemy_pokemon()
        battle_menu(Your_pokemon, the_enemy)

    else:
        move_player(player_location)


def enemy_pokemon():
    Random_pokemon = [Pokemon("Pidgey", 5, "flying", "Female", 7000, 1000),
    Pokemon("Ratata", 5, "normal", "Male", 5000, 1000),
    Pokemon("Caterpie", 5, "bug", "Female", 4000, 1000),
    Pokemon("Weedle", 5, "bug", "Male", 8000, 1000),
    Pokemon("Jude the Banisher", 100, "Lecturer", "Alpha Male", 10000, 30000)]
    x = Random_pokemon[random.randint(0,4)]
    print("A/An {} has appeared!".format(x.display_name()))
    return x


def battle_menu(Your_pokemon, the_enemy):
    print("What do you want to do:\n1. Enemy info\n2. Battle\n3. Catch\n4. Run")
    battle_catch_run=input("Number of choice: ")
    if battle_catch_run == "1":
        the_enemy.display_info()
        battle_menu(Your_pokemon, the_enemy)

    elif battle_catch_run == "2":
        battle(Your_pokemon, the_enemy)

    elif battle_catch_run == "3":
        catch(the_enemy)

    elif battle_catch_run == "4":
        run(the_enemy)

    else:
        print("Choose action from options!")
        battle_menu(Your_pokemon, enemy_pokemon)


def battle(Your_pokemon, the_enemy):
    z = int(choose_pokemon(Your_pokemon, the_enemy))
    x = int(the_enemy.get_hp())
    y = Your_pokemon[z].hp
    while x > 0 and y > 0:
        if y > 0:
            print("{} attack!".format(Your_pokemon[z].name))
            x = int(x) - int(Your_pokemon[z].damage)
            print("Enemy hp: "+str(x)+"\n")
            if x > 0:
                print("{} attack!".format(the_enemy.name))
                y = y-the_enemy.damage
                print("Your pokemon's hp: "+str(y)+"\n")

            else:
                continue
    Your_pokemon[z].hp = y
    if x <= 0:
        print("The enemy has fainted!")
        exp_before = Your_pokemon[z].get_exp()
        Your_pokemon[z].add_exp()
        print("{} gained {} exp\n".format(Your_pokemon[z].name, int(Your_pokemon[z].get_exp())-int(exp_before)))
        if Your_pokemon[z].get_exp() >= 100:
            print("{} level up!".format(Your_pokemon[z].name))
            Your_pokemon[z].add_level()
            Your_pokemon[z].add_damage()
        move_player(player_location)

    elif y <= 0:
        print("Your pokemon has fainted!")
        Your_pokemon.remove(z)
        end_of_game()
        print("Pokemon(s) left {}".format(len(Your_pokemon)))
        print("Your other pokemon are afraid to fight because you fight recklessly...")
        print("You decided to run..\n")
        move_player(player_location)

def end_of_game():
    if len(Your_pokemon) == 0:
        print("Game Over!")

def choose_pokemon(Your_pokemon, the_enemy):
    print("Your pokemon:  ")
    for i in range (0, len(Your_pokemon)):
        print("{}. {}".format(i+1, Your_pokemon[i].display_name()))
    ans = input("Action:\n1. Info of your pokemon\n2. Choose pokemon\n3. Back\nYour action: ")
    if ans == "1":
        Your_pokemon[choose_poke_number(Your_pokemon)].display_info()
        choose_pokemon(Your_pokemon, the_enemy)

    elif ans == "2":
        return choose_poke_number(Your_pokemon)

    elif ans == "3":
        battle_menu(Your_pokemon, the_enemy)

    else:
        choose_pokemon(Your_pokemon, the_enemy)

def choose_poke_number(Your_pokemon):
    pokenum=input("Input your pokemon number:\n")
    try:
        if int(pokenum)==0:
            print("Choose from the list!")
            choose_poke_number(Your_pokemon)
        else:
            return int(pokenum)-1
    except:
        print("Choose from the list!")
        choose_poke_number(Your_pokemon)

def catch(the_enemy):
    if len(Your_pokemon)<=5:
        chance=random.randint(0, 100)
        if chance>=70:
            print("You successfully catch {}".format(the_enemy.display_name()))
            Your_pokemon.append(YourPokemon(the_enemy.name, the_enemy.get_level(), the_enemy.type, the_enemy.gender, the_enemy.hp, 0, the_enemy.damage))
            move_player(player_location)
        else:
            print("You failed to catch {}".format(the_enemy.display_name()))
            battle_menu(Your_pokemon, the_enemy)
    else:
        print("Can't catch anymore pokemon, max number of pokemon = 6!")
        battle_menu(Your_pokemon, the_enemy)

def run(the_enemy):
    chance=random.randint(0, 100)
    if chance>=60:
        print("You got away safely...")
        move_player(player_location)
    else:
        print("You failed to run away...")
        battle_menu(Your_pokemon, the_enemy)

main()
