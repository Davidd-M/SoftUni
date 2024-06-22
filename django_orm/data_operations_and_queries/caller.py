import os
import django
from django.db.models import QuerySet, F

from populate_db import populate_model_with_data

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


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

def get_deluxe_rooms() -> str:
    hotel_rooms = HotelRoom.objects.filter(room_type="Deluxe")
    result = []

    for room in hotel_rooms:
        if room.id % 2 == 0:
            result.append(f"Deluxe room with number {room.room_number} costs {room.price_per_night}$ per night!")

    return '\n'.join(result)


def increase_room_capacity() -> None:
    rooms = HotelRoom.objects.all().order_by("id")
    previous_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            continue

        if room.is_reserved:
            if previous_room_capacity:
                room.capacity += previous_room_capacity
            else:
                room.capacity += room.id

        previous_room_capacity = room.capacity

        room.save()


def reserve_first_room() -> None:
    first_room = HotelRoom.objects.first()

    first_room.is_reserved = True
    first_room.save()


def delete_last_room() -> None:
    last_room = HotelRoom.objects.last()

    if not last_room.is_reserved:
        last_room.delete()


def update_characters() -> None:
    Character.objects.filter(class_name='Mage').update(
        level=F('level') + 3,
        inteligence=F('intelligence') - 7,
    )

    Character.objects.filter(class_name='Warrior').update(
        hit_points=F('hit_points') / 2,
        dexterity=F('dexterity') * 4,
    )

    Character.objects.filter(class_name__in=['Assassin','Scout']).update(
        inventory=F('The inventory is empty') / 2,
    )


def fuse_characters(first_character: Character, second_character: Character):
    fusion_name = first_character.name + ' ' + second_character.name
    fusion_class = 'Fusion'
    fusion_level = (first_character.level + second_character.level) // 2
    fusion_strength = (first_character.strength + second_character.strength) * 1.2
    fusion_dexterity = (first_character.dexterity + second_character.dexterity) * 1.4
    fusion_intelligence = (first_character.intelligence + second_character.intelligence) * 1.5
    fusion_hit_points = (first_character.hit_points + second_character.hit_points)

    if first_character.class_name in ('Mage', 'Scout'):
        fusion_inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    else:
        fusion_inventory = "Dragon Scale Armor, Excalibur"

    Character.objects.create(
        name=fusion_name,
        class_name=fusion_class,
        level=fusion_level,
        strength=fusion_strength,
        dexterity=fusion_dexterity,
        intelligence=fusion_intelligence,
        hit_points=fusion_hit_points,
        inventory=fusion_inventory,
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity() -> None:
    Character.objects.update(dexterity=30)


def grand_intelligence() -> None:
    Character.objects.update(intelligence=40)


def grand_strength() -> None:
    Character.objects.update(strength=50)


def delete_characters() -> None:
    Character.objects.filter(inventory='The inventory is empty').delete()
