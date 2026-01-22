
class person:
    def move(self):
        print("Move 4 peaces")
    def rest(self):
        print("Gains 4 health points")

class Doctor(person):
    def heal(self):
        print("10 Points")


class Fighter(person):
    def fight(self):
        print("10 Points for damage")


class Wizard(Doctor,Fighter):
    def cast_spell(self):
        print("Turn Invisible")

    def heal(self):
         print("Health points 15")



char1 = Fighter()
char1.move()
