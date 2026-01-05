# 🐾 Dog Bus Tracker — Challenge Steps
#
# 1. Start with a bus dictionary holding current passengers.
#    - Each seat number (1, 2, 3, ...) is a key
#    - Each value is another dictionary with each pet's:
#        • name
#        • breed
#        • pickup time
#        • dropoff time
#
# 2. Print a starting roster showing each pet’s seat, name, and pickup time.
#
# 3. Add one new pet if there’s room on the bus.
#    - Use MAX_SEATS to limit capacity.
#    - Dynamically assign the next seat number.
#    - Print the updated roster showing all pets after pickup.
#
# 4. Ask which pet leaves early.
#    - Remove that pet from the bus.
#    - Print a message saying they’ve headed home.
#
# 5. Print a final roster listing the remaining pets and their dropoff times.


max_seats = 8
bus = {
    1: {"name": "Milo", "breed": "Labrador", "pickup": "8:00 AM", "dropoff": "4:00 PM"},
    2: {"name": "Otis", "breed": "French Bulldog", "pickup": "8:15 AM", "dropoff": "4:15 PM"},
    3: {"name": "Willow", "breed": "Border Collie", "pickup": "8:30 AM", "dropoff": "4:30 PM"},
}
