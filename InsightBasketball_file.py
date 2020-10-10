class Basketball:
    def __init__(self, name, position, points):
        self.name = name
        self.position = position
        self.points = points 

    def __str__(self):
        return f"{self.name} is a {self.position} and he scored {self.points} This match"

    def average_Points(self, total):
        return total/5

    def way_To_score(self, way):
        return f"{self.name} mostly scores by {way}"

class PointGuard(Basketball):
    def way_To_score(self, way="shooting"):
        return super().way_To_score(way)

class ShootingGuard(Basketball):
    def way_To_score(self, way="shooting"):
        return super().way_To_score(way)

class SmallForward(Basketball):
    def way_To_score(self, way="slashing"):
        return super().way_To_score(way)

class PowerForward(Basketball):
    def way_To_score(self, way="driving"):
        return super().way_To_score(way)

class Center(Basketball):
    def way_To_score(self, way="fading"):
        return super().way_To_score(way)



Josh = PointGuard("Josh", "PG", 18)

Figo = ShootingGuard("Figo", "SG", 18)

Ravin = SmallForward("Ravin", "SF", 10)

Bob = PowerForward("Bob", "PF", 12)

Gary = Center("Gary", "C", 15)

print ("This is the Insight basketball team. \n")

print ("Choose your character.\n")

print ("- Josh")

print ("- Figo")

print ("- Ravin")

print ("- Bob")

print ("- Gary\n")

Player = input()

print("\n")

if Player == "Josh":
    print(Josh)
    print("his average points are: ")
    print(Josh.average_Points(100))
    print(Josh.way_To_score())
    print("\n")

elif Player == "Figo":
    print(Figo)
    print("his average points are: ")
    print(Figo.average_Points(80))
    print(Figo.way_To_score())
    print("\n")

elif Player == "Ravin":
    print(Ravin)
    print("his average points are: ")
    print(Ravin.average_Points(60))
    print(Ravin.way_To_score())
    print("\n")

elif Player == "Bob":
    print(Bob)
    print("his average points are: ")
    print(Ravin.average_Points(50))
    print(Bob.way_To_score())
    print("\n")

elif Player == "Gary":
    print(Gary)
    print("his average points are: ")
    print(Gary.average_Points(70))
    print(Gary.way_To_score())
    print("\n")


else:
    print("Player not available")
