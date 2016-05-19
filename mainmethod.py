import random

def get_dialogue_text(choice):
    """
        :param choice(str): The dialogue tree and section of the ship that the player will explore.

        :returns: A list containing each dialogue item/user decision start.
    """
    file_extension = ".txt"

    with open(choice + file_extension, 'r') as f:
        dialogue = f.read()

    return dialogue


def explore_branch(choice):
    """
        :param choice(str): The dialogue tree and section of the ship that the player will explore.

    """
    dialogue_tree = get_dialogue_text(choice)
    print(dialogue_tree)
    alive = True
    current_step = 0

    # do game stuff for this specific branch
    while alive:
        alive = make_choice(current_step, dialogue_tree[current_step])
        current_step += 1


def make_choice(current_step, dialogue_tree_item):
    """
        :param current_step(int): Which dialogue item the player is currently on
        :param dialogue_tree_item(str): String containing the dialogue for the
                                        current step and the choice the user can make

        :returns: bool, alive or dead (true or false)

    """
    # present decision to user
    # have the user make a decision
    direction = input("Which direction do you go? [L/R]L").upper()
    return direction




# Constants
player_health = 20
alien_health = 10
title_bar = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
title = "\nWelcome aboard the UNSC Aurora, the only surviving destroyer in the entire UNSC fleet.\n"
initial_decision = "You are faced with 3 signs. One leads to the captains quarters, one leads to the logistics bay," \
" and the other to the ship hangar.\n"
correct_choices = ['L', 'C', 'S']
print(title_bar + title + title_bar)
choice = None  # non-valid default choice
print(initial_decision)
while choice not in correct_choices:
    choice = input("Which one do you go to? [{}]: ".format("/".join(correct_choices))).upper()  # uppercase conversion
explore_branch(choice)