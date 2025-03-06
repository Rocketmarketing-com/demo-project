import pandas as pd


class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am a {self.species}.")


dog = Pet(name="Buddy", species="Dog")
cat = Pet(name="Harry", species="Cat")

dog.species
cat.name
dog.introduce()

df = pd.DataFrame({"A": [1, 2, 4], "B": [1, 2, 3]})
df2 = pd.DataFrame({"A": [1, 2, 3], "B": [1, 2, 3]})
