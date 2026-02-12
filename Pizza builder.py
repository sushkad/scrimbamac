class Pizza:
    def __init__(self, size, crust):
        self.size = size
        self.crust = crust
        self.toppings = []  # empty list initially

    # Step 2: Add topping
    def add_topping(self, topping):
        if topping not in self.toppings:
            self.toppings.append(topping)
            print(f"{topping} added.")
        else:
            print(f"{topping} already added.")

    # Step 3: Remove topping
    def remove_topping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)
            print(f"{topping} removed.")
        else:
            print(f"{topping} not found on pizza.")

    # Step 4: Print pizza details
    def print_details(self):
        print("\n🍕 Pizza Summary")
        print(f"Size: {self.size}")
        print(f"Crust: {self.crust}")

        if self.toppings:
            print("Toppings:", ", ".join(self.toppings))
        else:
            print("Toppings: No toppings yet!")



# Create pizza object
my_pizza = Pizza("Large", "Thin Crust")

# Customize pizza
my_pizza.add_topping("Cheese")
my_pizza.add_topping("Mushrooms")
my_pizza.add_topping("Olives")
my_pizza.remove_topping("Mushrooms")

# Print summary
my_pizza.print_details()
