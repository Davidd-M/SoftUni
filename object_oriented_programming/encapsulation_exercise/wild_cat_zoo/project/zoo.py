from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.__workers_capacity = workers_capacity
        self.__animal_capacity = animal_capacity
        self.__budget = budget
        self.name = name
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__budget < price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"

        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name) -> str:
        try:
            worker = next(filter(lambda x: x.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        salaries = 0

        for worker in self.workers:
            salaries += worker.salary

        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        amount = 0

        for animal in self.animals:
            amount += animal.money_for_care

        if self.__budget >= amount:
            self.__budget -= amount
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        animals_dict = {"Lion": [0], "Tiger": [0], "Cheetah": [0]}
        result = f"You have {len(self.animals)} animals"

        for animal in self.animals:
            animals_dict[animal.__class__.__name__][0] += 1
            animals_dict[animal.__class__.__name__].append(f"\n{animal.__repr__()}")

        for animal in animals_dict.keys():
            result += f"\n----- {animals_dict[animal][0]} {animal}s:"
            for rep in animals_dict[animal][1::]:
                result += f"{rep}"

        return result

    def workers_status(self) -> str:
        workers_dict = {"Keeper": [0], "Caretaker": [0], "Vet": [0]}
        result = f"You have {len(self.workers)} workers"

        for worker in self.workers:
            workers_dict[worker.__class__.__name__][0] += 1
            workers_dict[worker.__class__.__name__].append(f"\n{worker.__repr__()}")

        for worker in workers_dict.keys():
            result += f"\n----- {workers_dict[worker][0]} {worker}s:"
            for rep in workers_dict[worker][1::]:
                result += f"{rep}"

        return result
