# adventure_game.py
# A text-based adventure game: the player is an explorer searching for a
# legendary treasure hidden in an ancient land. They choose between a dark
# forest and a mysterious cave, and every decision leads to a win, a loss,
# or a setback. Demonstrates variables, lists, loops, conditionals and functions.

# Task 1: simple print statement to confirm the setup is working
print("Adventure game loaded successfully!\n")

# Items the player collects during one playthrough (reset on every restart)
inventory = []


def get_choice(prompt, options):
    """Ask the player to pick one of the options and keep asking until valid.

    options is a list of valid answers, e.g. ["forest", "cave"].
    The player may type the word or its number (1, 2, ...).
    """
    while True:
        answer = input(f"{prompt} ({' / '.join(options)}): ").strip().lower()
        if answer in options:
            return answer
        # Allow numeric shortcuts: 1 = first option, 2 = second option ...
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return options[int(answer) - 1]
        print(f"  Please type one of: {', '.join(options)}.")


def show_inventory():
    """Print the items the player is currently carrying."""
    if inventory:
        print(f"  [Inventory: {', '.join(inventory)}]")
    else:
        print("  [Inventory: empty]")


def start_game():
    """Introduce the quest, ask for the player's name and offer the first choice.

    Returns True if the player finds the treasure, False otherwise.
    """
    inventory.clear()

    print("=" * 60)
    print("        THE LEGEND OF THE LOST TREASURE")
    print("=" * 60)
    print("Long ago, a great treasure was hidden in an ancient land.")
    print("Many explorers have searched for it. None have returned.\n")

    player_name = input("What is your name, explorer? ").strip().title()
    if not player_name:
        player_name = "Explorer"

    print(f"\nWelcome, {player_name}! Your quest is to find the legendary treasure.")
    print("You stand at a crossroads. To the left lies a DARK FOREST.")
    print("To the right, the mouth of a MYSTERIOUS CAVE.\n")

    choice = get_choice("Which path will you explore?", ["forest", "cave"])

    if choice == "forest":
        return forest_path(player_name)
    else:
        return cave_path(player_name)


def forest_path(player_name):
    """Forest scenario: follow the river or climb a tree."""
    print("\n--- THE DARK FOREST ---")
    print("Tall trees block out the sun. You hear rushing water nearby,")
    print("and notice a giant tree with low branches you could climb.\n")

    choice = get_choice("What do you do?", ["river", "tree"])

    if choice == "river":
        print("\nYou follow the river until it reaches a wide, fast crossing.")
        print("On the far bank you can see old stone steps leading uphill.\n")
        crossing = get_choice("How do you cross?", ["raft", "swim"])

        if crossing == "raft":
            print("\nYou tie fallen logs together with vines and paddle across.")
            print("The stone steps lead to a hidden shrine. Inside, a golden")
            print(f"chest gleams in the light. You found the treasure, {player_name}!")
            return True
        else:
            print("\nThe current is far stronger than it looked. You are swept")
            print("downstream and wash up miles away, your supplies lost.")
            return False
    else:
        print("\nYou climb to the top of the tree. From here you spot the ruins")
        print("of an old temple to the north, and you find a rolled-up MAP")
        print("wedged in a hollow branch!")
        inventory.append("map")
        show_inventory()
        print()
        next_step = get_choice("Where do you go next?", ["temple", "rest"])

        if next_step == "temple":
            print("\nUsing the map, you avoid a hidden pit trap and reach the temple.")
            print("Behind the altar sits a chest overflowing with gold.")
            print(f"You found the treasure, {player_name}!")
            return True
        else:
            print("\nYou rest under the tree and fall asleep. When you wake, night")
            print("has fallen and you are hopelessly lost in the dark forest.")
            return False


def cave_path(player_name):
    """Cave scenario: light a torch or proceed in the dark."""
    print("\n--- THE MYSTERIOUS CAVE ---")
    print("Cold air drifts out of the cave. It is pitch black inside.")
    print("An unlit torch rests in a bracket near the entrance.\n")

    choice = get_choice("What do you do?", ["torch", "dark"])

    if choice == "torch":
        inventory.append("torch")
        print("\nThe torch flares to life, revealing two tunnels.")
        show_inventory()
        print("The LEFT tunnel has ancient symbols carved into the wall.")
        print("The RIGHT tunnel glitters with something shiny on the floor.\n")
        tunnel = get_choice("Which tunnel do you take?", ["left", "right"])

        if tunnel == "left":
            print("\nThe symbols are a guide left by the treasure's makers. You")
            print("follow them to a vast chamber where a jewelled chest awaits.")
            print(f"You found the treasure, {player_name}!")
            return True
        else:
            print("\nThe shiny objects are only wet stones. As you step forward,")
            print("the floor gives way and the tunnel collapses behind you.")
            return False
    else:
        print("\nYou feel your way forward in total darkness...")
        print("Your foot finds nothing but air, and you tumble into a deep pit.")
        return False


def main():
    """Run the game in a loop until the player wins or decides to stop."""
    attempts = 0
    playing = True

    while playing:
        attempts += 1
        won = start_game()

        if won:
            print("\n*** CONGRATULATIONS! YOU WIN! ***")
            print(f"Quest completed in {attempts} attempt(s).")
            again = get_choice("\nWould you like to play again?", ["yes", "no"])
        else:
            print("\n*** GAME OVER - your adventure ends here. ***")
            again = get_choice("\nWould you like to restart and try again?", ["yes", "no"])

        if again == "no":
            playing = False
        else:
            print()

    print("\nThanks for playing. Farewell, explorer!")


# Task 5: start the adventure
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nGame exited. Farewell, explorer!")
