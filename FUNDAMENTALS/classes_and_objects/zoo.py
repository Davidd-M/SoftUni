class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        self.__animals += 1
        if species == "mammal":
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        else:
            self.birds.append(name)

    def get_info(self, species):
        if species == "fish":
            species = species + "es"
        else:
            species = species + "s"
        specie_list = getattr(self, species)
        names = [a for a in specie_list]
        return (f"{species.capitalize()} in {self.zoo_name}: {', '.join(names)}\n"
                f"Total animals: {int(self.__animals)}")


current_zoo_name = input()
zoo = Zoo(current_zoo_name)
animals = int(input())
for animal in range(animals):
    specie, animal_name = input().split()
    zoo.add_animal(specie, animal_name)
specie_to_print = input()
print(zoo.get_info(specie_to_print))
