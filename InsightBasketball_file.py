class basketball:
    def __init__(self, name, position, points):
        self.name = name
        self.position = position
        self.points = points 

    def __str__(self):
        return f"{self.name} is a {self.position} and he scored {self.points} This match"

    def averagePoints(self, total):
        return total/5

    def way_To_score(self, way):
        return f"{self.name} mostly scores by {way}"

class pointGuard(Basketball):
    def way_To_score(self, way="shooting"):
        return super().way_To_score(way)

class shootingGuard(Basketball):
    def way_To_score(self, way="shooting"):
        return super().way_To_score(way)

class smallForward(Basketball):
    def way_To_score(self, way="slashing"):
        return super().way_To_score(way)

class powerForward(Basketball):
    def way_To_score(self, way="driving"):
        return super().way_To_score(way)

class center(Basketball):
    def way_To_score(self, way="fading"):
        return super().way_To_score(way)



Josh = pointGuard("Josh", "PG", 18)

Figo = shootingGuard("Figo", "SG", 18)

Ravin = smallForward("Ravin", "SF", 10)

Bob = power_Forward("Bob", "PF", 12)

Gary = center("Gary", "C", 15)

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
    print(Josh.averagePoints(100))
    print(Josh.way_To_score())
    print("\n")

elif Player == "Figo":
    print(Figo)
    print("his average points are: ")
    print(Figo.averagePoints(80))
    print(Figo.way_To_score())
    print("\n")

elif Player == "Ravin":
    print(Ravin)
    print("his average points are: ")
    print(Ravin.averagePoints(60))
    print(Ravin.way_To_score())
    print("\n")

elif Player == "Bob":
    print(Bob)
    print("his average points are: ")
    print(Ravin.averagePoints(50))
    print(Bob.way_To_score())
    print("\n")

elif Player == "Gary":
    print(Gary)
    print("his average points are: ")
    print(Gary.averagePoints(70))
    print(Gary.way_To_score())
    print("\n")


else:
    print("Player not available")

