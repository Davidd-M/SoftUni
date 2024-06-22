import os
import django
from django.db.models import QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location


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

print(show_all_locations())
print(new_capital())
print(get_capitals())
