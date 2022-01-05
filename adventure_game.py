import time
import random

randomized = {
    "villain": "",
    "snacks": "",
    "drink": ""
    }


def randomChoice():
    villians = random.choice(["Pirates", "gorgon", "troll", "fairy"])
    snack = random.choice(["Cookies", "Oat", "Soup", "Pizza"])
    drinks = random.choice(["beer", "gin", "water", "Soda"])
    randomized["villain"] = villians
    randomized["snacks"] = snack
    randomized["drink"] = drinks


def print_pause(messages, sleep):

    print(messages)
    time.sleep(sleep)


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!', 2)


def restart():

    play_again = valid_input("Would you like to play again?\n"
                             "Enter y/n\n", ['y', 'n'])
    if play_again == "y":
        play_game()
    elif play_again == "n":
        print_pause("Thank you for playing.", 2)
    print_pause("Goodbye!", 2)


def intro():
    villian = randomized["villain"]
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.", 2)
    print_pause(f"Rumor has it that a wicked {villian} is somewhere "
                "around here, and has been "
                "terrifying the entire village.", 2)
    print_pause("You are lost, hungry and famished.", 2)
    print_pause("In front of you is a House.", 2)
    print_pause("To your right is a Church.", 2)
    print_pause("In your hand you hold the keys "
                "to your car that you parked a mile behind .", 2)


def church(item):

    if "key" in item:
        print_pause("You move cautiously into the Church.", 2)
        print_pause("You've been here before, and met with the preacher, "
                    "he has given you something", 2)
        print_pause("Preacher wants to pray, he asks you to leave", 2)
        game(item)
    else:
        print_pause("You move cautiously into the Church.", 2)
        print_pause("It turns out to be only a very small Church.", 2)
        print_pause("Your eye catches a glint of someone behind a desk.", 2)
        print_pause("You have found the Preacher of the Church", 2)
        print_pause("He gives you the key to the house adjacent "
                    "the Church.", 2)
        item.append("key")
    print_pause("You walk back out to the field.", 2)
    game(item)


def house(item):

    drink = randomized["drink"]
    snacks = randomized["snacks"]

    print_pause("You approach the door of the house.", 2)
    print_pause("You are about to knock when the door "
                "opens.", 2)
    print_pause("Eep! This is a creepy house!", 2)
    print_pause("You are scared to enter the house.", 2)
    print_pause("You remember the rumors, "
                "but you need a place to rest and something to eat", 2)
    enter_or_run = valid_input("Would you like to "
                         "(1) enter the house or (2) run away?\n", ['1', '2'])
    if enter_or_run == "2":
        print_pause("You run back into the field. Luckily, "
                    "nothing seem to be chasing you.", 2)
        game(item)

    elif enter_or_run == "1":
        print_pause("You enter the house, "
                    "it is a nice apartment", 2)
        print_pause("There is a chair in the living room,"
                    " a dinner and kitchen behind the dinner.", 2)
        print_pause("Your stomach rumbles. you walk to"
                    " the kitchen, there you find a fridge!", 2)
        open_fridge = valid_input("Would you like to open the fridge?\n"
                            "Enter y/n\n", ['y', 'n'])
        if open_fridge == "y":
            if "key" in item:
                print_pause("You open the refrigerator.", 2)
                print_pause("You get excited. Alas! "
                            "something to eat.", 2)
                print_pause(f"You pick up a bottle of {drink}"
                            f" and some {snacks}", 2)
                print_pause("You walk back to the living room.", 2)
                print_pause("You sit on the chair to eat.", 2)
                print_pause("After eating, you lay on the chair and sleep.", 2)
                restart()

            else:
                print_pause("You cannot open the fridge, "
                            "go back to the church.", 2)
                game(item)

        elif open_fridge == "n":
            print_pause("You walk back to the living room.", 2)
            print_pause("You lay on the chair and sleep.", 2)
            restart()

    
def game(item):

    response = valid_input("Enter 1 to knock on the door of the House.\n"
                     "Enter 2 to peer into the Church.\n"
                     "What would you like to do?\n"
                     "(Please enter 1 or 2.)\n", ['1', '2'])
    if response == "1":
        house(item)

    elif response == "2":
        church(item)

    else:
        game(item)


def play_game():

    item = []
    randomChoice()

    intro()

    game(item)


play_game()
