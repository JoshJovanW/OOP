class Heroes:
    def __init__(self, name, age, powers):
        self.name = name
        self.age = age
        self.powers = powers

    def __str__(self):
        return f"{self.name} is {self.age} years old and has {self.powers} ability"

    def skill(self, skills):
        return f"{self.name} powers are {self.powers} he can {skills} the enemy."


class Cyro(Heroes):
    def skill(self, skills="freeze"):
        return super().skill(skills)

class Pyro(Heroes):
    def skill(self, skills="burn"):
        return super().skill(skills)

Kaede = Cyro("kaede", 20, "Cyrokinesis")

LangLing = Pyro("LangLing", 18, "Pyrokinesis")

print("This is an introduction manual for the heroes.\n")

print("Pick a hero\n")

print("Kaede or Langling")

hero = input()

print("\n")


if hero == "Kaede":
    print(Kaede)
    print("these are his skills.\n")
    print(Kaede.skill())

else:
    print(LangLing)
    print("these are her skills.\n")
    print(LangLing.skill())
