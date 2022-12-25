import minigames.joust as joust
import minigames.melee as melee
from town import Town
from Character import Character
from Location import Location
from TextGenerator import stream_print


def main():
    character_name = input("Welcome to Argyle, please input your name.\n")
    town_name = "Sorenthal"

    if character_name:
        print("Thank you.") 
        player_character = Character(name=character_name)
    else:
        print("No name specified. Generating random character...\n")
        player_character = Character()
    
    my_town = generate_town(
        town_name,
        tournament=True,
        melee=True,
    )

    while(True):
        print(f"\nWelcome to {town_name}, {player_character.name}. " \
            + "You stand in the town square." \
        )

        describe_town(
            my_town, 
            player_character.name
        )

        response = input()
       
        #FIXME
        if response == "0":
            if player_character.description != "":
                stream_print(player_character.description, 0)
            else: 
                player_character.generate_and_stream_description()

        if response == "1":
            go_jousting(player_character.name)
            break
        if response == "2":
            go_melee(player_character.name)
        else:
            print("\n============= not yet implemented, sorry ==============\n")
            continue

def go_jousting(
        combatant_A_name="",
        combatant_B_name="",
):
    new_joust = joust.Joust(
        combatant_A_name,
        combatant_B_name,
    )

    new_joust.main_joust()

def go_melee(name=""):
    melee.main_melee(name)

def generate_town(
    town_name, 
    tournament, 
    melee
):
    town = Town(
        name=town_name,
        tournament=tournament,
        melee=melee,
    )

    return town

def describe_town(
    town, 
    player_name
):
    town.describe_town(player_name)

    actions = "\n\n=========== Actions =============" \
        + "\n[0] = Describe Character" \
        + "\n[1] = Visit the jousting tournament" \
        + "\n[2] = Visit the grand melee" \
        + "\n[3] = Visit the Tavern" \
        + "\n[4] = Explore the forest" \
        + "\n[5] = Visit the Mage Tower" \
        + "\n[6] = Visit the Night Market" \
        + "\n[7] = Explore the Underbelly" \
        + "\n[8] = Visit the Palace" \
        + "\n[9] = More..."

    print(actions)

def test_character_status(
    name="test-name",
    character_class="",
    description=""
):
    print("Now engaging character status test. Please stand by.\n")
    print("================== generating character ======================")
    test_character = Character(
        name,
        character_class,
        description
    )
    print("================== printing test character ===================")
    print(test_character)
    print("================== description ===============================")
    print(test_character.description)
    print("================== status ====================================")
    print(test_character.status)

    return test_character

def test_melee():
    print("Now engaging melee test. Please stand by.")
    user_character = test_character_status(
        name="user",
        character_class="commoner",
        description="unremarkable",
    )

    comp_character = test_character_status(name="comp")
    my_town = generate_town(
        town_name="Sorenthal",
        tournament=True,
        melee=True
    )

    print("Testing melee now...:")
    my_melee = melee.melee()
    my_melee.test_melee(
        user_character,
        comp_character
    )

def test_town():
    print("This is a test of the town functionality.")
    print("Please stand by as a town is generated.")

    town_name = "Sorenthal"
    my_town = generate_town(
        town_name="Sorenthal",
        tournament=True,
        melee=True
    )

    while(True):
        print(f"Welcome to {town_name}. You stand in the town square.")
        my_town.generate_and_stream_description()
        response = input()

def test_joust():
    print("This is a test of the joust functionality.")
    print("Please stand by as a joust is generated.")

    go_jousting("Aethelric, the strong")

#FIXME
def test_clock():
    while(True):
        break

def test_location():
    print("This is a test of the location functionality.")
    print("Please stand by as a location is generated and streamed.")
    my_loc = Location()
    my_loc.describe()

main()
#test_location()
#test_character_status
#test_melee()
#test_town()
#test_joust()
#test_clock()

