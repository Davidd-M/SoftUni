import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Astronaut, Mission, Spacecraft
from django.db.models import Q, Count, Sum, Avg, F
from django.db.models.functions import Coalesce


def get_astronauts(search_string=None):
    if search_string is None:
        return ""

    astronauts = Astronaut.objects.filter(
        Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)
    ).order_by('name')

    if not astronauts.exists():
        return ""

    result = []
    for astronaut in astronauts:
        status = "Active" if astronaut.is_active else "Inactive"
        result.append(f"Astronaut: {astronaut.name}, phone number: {astronaut.phone_number}, status: {status}")

    return "\n".join(result)


def get_top_astronaut():
    astro = Astronaut.objects.get_astronauts_by_missions_count().first()

    if not astro or astro.missions_count == 0:
        return "No data."

    return f"Top Astronaut: {astro.name} with {astro.missions_count} missions."

def get_most_used_spacecraft():
    spacecraft = (Spacecraft.objects
                  .annotate(num_missions=Count('mission'))
                  .order_by('-num_missions', 'name')
                  .first())

    if not spacecraft or spacecraft.num_missions == 0:
        return "No data."

    unique_astronauts = Astronaut.objects.filter(mission_astronauts__spacecraft=spacecraft).distinct().count()

    return (f"The most used spacecraft is: {spacecraft.name}, manufactured by {spacecraft.manufacturer}, "
            f"used in {spacecraft.num_missions} missions, astronauts on missions: {unique_astronauts}.")


def get_last_completed_mission():
    mission = (Mission.objects.filter(status='Completed')
               .annotate(space_walks=Sum('astronauts__spacewalks')).
               order_by('-launch_date').first())

    if mission is None:
        return "No data."

    astronauts = [a.name for a in mission.astronauts.all().order_by('name')]

    return (f"The last completed mission is: {mission.name}. "
            f"Commander: {mission.commander.name if mission.commander else 'TBA'}. "
            f"Astronauts: {', '.join(astronauts)}. "
            f"Spacecraft: {mission.spacecraft.name}. "
            f"Total spacewalks: {mission.space_walks}.")


def decrease_spacecrafts_weight():
    spacecrafts = Spacecraft.objects.filter(
        spacecrafts_usage__status='Planned',
        weight__gte=200.0
    ).distinct()

    if not spacecrafts.exists():
        return "No changes in weight."

    for spacecraft in spacecrafts:
        spacecraft.weight -= 200.0
        spacecraft.save()

    avg_weight = Spacecraft.objects.all().aggregate(avg_weight=Avg('weight'))['avg_weight']
    num_of_spacecrafts = spacecrafts.count()

    return (f"The weight of {num_of_spacecrafts} spacecrafts has been decreased. "
            f"The new average weight of all spacecrafts is {avg_weight:.1f}kg")
