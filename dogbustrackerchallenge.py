# 🐾 Dog Bus Tracker — Challenge Steps

MAX_SEATS = 8

bus = {
    1: {"name": "Milo", "breed": "Labrador", "pickup": "8:00 AM", "dropoff": "4:00 PM"},
    2: {"name": "Otis", "breed": "French Bulldog", "pickup": "8:15 AM", "dropoff": "4:15 PM"},
    3: {"name": "Willow", "breed": "Border Collie", "pickup": "8:30 AM", "dropoff": "4:30 PM"},
}

print("-- Starting Roster --")
for seat, info in bus.items():
    print(f"Seat {seat}: {info['name']} (pickup {info['pickup']})")

# Add a new pet if space is available
if len(bus) < MAX_SEATS:
    seat_num = max(bus.keys()) + 1
    new_pet = {
        "name": "Sir Bark-a-Lot",
        "breed": "Corgi Knight",
        "pickup": "8:45 AM",
        "dropoff": "4:45 PM",
    }
    bus[seat_num] = new_pet
    print(f"\n{new_pet['name']} boards the bus (Seat {seat_num})")
else:
    print("\nNo free seats available.")

print("\n-- Roster After Pickup --")
for seat, info in bus.items():
    print(f"Seat {seat}: {info['name']}")

# Remove a pet who goes home early
remove_name = input("\nWho goes home early? ").strip().lower()
seat_to_remove = None

for seat, info in bus.items():
    if info["name"].lower() == remove_name:
        seat_to_remove = seat
        break

if seat_to_remove:
    gone = bus.pop(seat_to_remove)
    print(f"\n{gone['name']} (Seat {seat_to_remove}) headed home early.")
else:
    print(f"\nNo passenger named '{remove_name}' on the bus.")

print("\n-- Final Roster --")
for seat, info in bus.items():
    print(f"Seat {seat}: {info['name']} (drop-off {info['dropoff']})")
