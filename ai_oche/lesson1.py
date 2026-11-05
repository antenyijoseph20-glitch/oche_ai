
location_map = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle"]
}

items_by_location = {
    "Beach": "Rope",
    "Jungle": "Lantern",
    "Cave": None
}

inventory = []

energy = 5
current_location = "Beach"
playing = True


def normalize_input(value):
    """Normalize input by removing whitespace and ignoring case."""
    return "".join(value.split()).casefold()


def beach_scene():
    global current_location, playing

    while playing:
        #print(f"\nThanks for playing! You left from {current_location}.")
        print("Current location:", current_location)
        print("Energy remaining:", energy)
        print("Available destinations:", location_map[current_location])
        #print("==============================")

        print("1. Move to another location")
        print("2. Check inventory")
        print("3. Collect item")
        print("4. Quit")

        choice = input("Choose: ").strip()

        if choice == "1":
            destination = input("Where do you want to go? ")

            normalized_destination = normalize_input(destination)

            valid_destinations = location_map[current_location]

            matched_destination = None

            for location in valid_destinations:
                if normalize_input(location) == normalized_destination:
                    matched_destination = location
                    break

            if matched_destination is not None:
                current_location = matched_destination
                print("You moved to", current_location)
            else:
                print("Invalid destination. You cannot move there.")

        elif choice == "2":
            if inventory:
                print("Your inventory:", inventory)
            else:
                print("Your inventory is empty.")

        elif choice == "3":
            item = items_by_location[current_location]

            if item is None:
                print("There are no items to collect here.")

            elif item in inventory:
                print("You have already collected the", item)

            else:
                inventory.append(item)
                print("You collected the", item)

        elif choice == "4":
            playing = False

        elif choice == "":
            print("Empty input. Please choose an option.")

        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")

    print(f"\nThanks for playing! You left from {current_location}.")

def create_new_game():
    inventory = []
    energy = 5
    current_location = "Beach"

    return inventory, energy, current_location



beach_scene()
