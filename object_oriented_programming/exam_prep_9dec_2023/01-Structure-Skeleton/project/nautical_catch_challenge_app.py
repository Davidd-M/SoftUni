from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    valid_divers = {
        "FreeDiver": FreeDiver,
        "ScubaDiver": ScubaDiver,
    }
    valid_fish_list = {
        "DeepSeaFish":DeepSeaFish,
        "PredatoryFish": PredatoryFish,
    }

    def __init__(self):
        self.divers: list = []
        self.fish_list: list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        try:
            instance = self.valid_divers[diver_type](diver_name)
        except KeyError:
            return f"{diver_type} is not allowed in our competition."

        if diver_name in [x.name for x in self.divers]:
            return f"{diver_name} is already a participant."

        self.divers.append(instance)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_name in [x.name for x in self.fish_list]:
            return f"{fish_name} is already permitted."

        try:
            instance = self.valid_fish_list[fish_type](fish_name, points)
        except KeyError:
            return f"{fish_type} is forbidden for chasing in our competition."

        self.fish_list.append(instance)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        try:
            diver = [d for d in self.divers if d.name == diver_name][0]
        except IndexError:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = [f for f in self.fish_list if f.name == fish_name][0]
        except IndexError:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            message = f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                message = f"{diver.name} hits a {fish.points}pt. {fish.name}."
            else:
                diver.miss(fish.time_to_catch)
                message = f"{diver_name} missed a good {fish_name}."
        else:
            diver.hit(fish)
            message = f"{diver_name} hits a {fish.points}pt. {fish_name}."

        if diver.oxygen_level == 0:
            diver.update_health_status()
        return message

    def health_recovery(self):
        recovered = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.has_health_issue = False
                diver.oxygen_level = diver.INITIAL_OXYGEN_LEVEL
                recovered += 1

        return f"Divers recovered: {recovered}"

    def diver_catch_report(self, diver_name: str):
        diver = next(filter(lambda x: x.name == diver_name, self.divers))
        fish_details = '\n'.join([fish.fish_details() for fish in diver.catch])
        return f"**{diver_name} Catch Report**\n" + fish_details

    def competition_statistics(self):
        healthy_divers = [d for d in self.divers if not d.has_health_issue]

        sorted_divers = sorted(
            healthy_divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name)
        )

        result = f"**Nautical Catch Challenge Statistics**\n"
        result += '\n'.join(str(d) for d in sorted_divers)
        return result
    