import os
import django
from django.db.models import QuerySet

from populate_db import populate_model_with_data

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location, Car, Task


def create_pet(name: str, species: str):

    Pet.objects.create(
        name=name,
        species=species,
    )

    return f"{name} is a very cute {species}!"


# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))

def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )

    return f"The artifact {name} is {age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name


def delete_all_artifacts():
    Artifact.objects.all().delete()

# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
# artifact_object = Artifact.objects.get(name='Ancient Sword')
# rename_artifact(artifact_object, 'Ancient Shield')
# print(artifact_object.name)


def show_all_locations() -> str:
    result = []

    for location in Location.objects.all().order_by("-id"):
        result.append(f"{location.name} has a population of {location.population}!")

    return '\n'.join(result)


def new_capital():
    first_location = Location.objects.first()
    if first_location is not None:
        first_location.is_capital = True
        first_location.save()


def get_capitals() -> QuerySet:
    return Location.objects.filter(is_capital=True).values("name")


def delete_first_location():
    Location.objects.first().delete()

# print(show_all_locations())
# print(new_capital())
# print(get_capitals())


def apply_discount():
    cars = Car.objects.all()

    for car in cars:
        discount = 0
        car_year = str(car.year)

        for digit in car_year:
            discount += int(digit)

        car.price_with_discount = float(car.price) - (float(car.price) * (discount / 100))
        car.save()


def get_recent_cars():
    return Car.objects.filter(year__gte=2021).values("model", "price_with_discount")


def delete_last_car():
    Car.objects.last().delete()

# apply_discount()
# print(get_recent_cars())


def show_unfinished_tasks():
    tasks = Task.objects.filter(is_finished=False)
    result = []

    for task in tasks:
        result.append(f"Task - {task.title} needs to be done until {task.due_date}!")

    return "\n".join(result)


def complete_odd_tasks() -> None:
    tasks = Task.objects.all()

    for task in tasks:
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str):
    tasks = Task.objects.filter(title=task_title)

    for task in tasks:
        task.description = ''.join(chr(ord(x) - 3) for x in text)
        task.save()


# encode_and_replace("Zdvk#wkh#glvkhv$", "Task 2")