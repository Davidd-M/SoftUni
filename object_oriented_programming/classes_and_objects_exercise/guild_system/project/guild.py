from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        for cur_player in self.players:
            if cur_player.name == player_name:
                cur_player.guild = "Unaffiliated"
                self.players.remove(cur_player)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = '\n'.join(f"{p.player_info()}" for p in self.players)
        return f"Guild: {self.name}\n" \
               f"{result}"


# from project.player import Player
# from project.guild import Guild
#
# import unittest
#
#
# class PlayerTest(unittest.TestCase):
#
#     def test_player_init(self):
#         player = Player("Pesho", 90, 90)
#         result = player.player_info().strip()
#         expected = "Name: Pesho\nGuild: Unaffiliated\nHP: 90\nMP: 90"
#         self.assertEqual(result, expected)
#
#     def test_adding_skill_should_work(self):
#         player = Player("Pesho", 90, 90)
#         message = player.add_skill("A", 3)
#         expected = "Skill A added to the collection of the player Pesho"
#         self.assertEqual(message, expected)
#
#     def test_adding_existing_skill_should_not_work(self):
#         player = Player("Pesho", 90, 90)
#         player.add_skill("A", 3)
#         message = player.add_skill("A", 3)
#         expected = "Skill already added"
#         self.assertEqual(message, expected)
#
#     def test_info(self):
#         player = Player("Pesho", 90, 90)
#         player.add_skill("A", 3)
#         message = player.player_info().strip()
#         expected = "Name: Pesho\nGuild: Unaffiliated\nHP: 90\nMP: 90\n===A - 3"
#         self.assertEqual(message, expected)
#
#     def test_guild_init(self):
#         guild = Guild("GGXrd")
#         message = guild.guild_info().strip()
#         expeted = "Guild: GGXrd"
#         self.assertEqual(message, expeted)
#
#     def test_assign_working(self):
#         guild = Guild("GGXrd")
#         player = Player("Pesho", 90, 90)
#         message = guild.assign_player(player)
#         expected = "Welcome player Pesho to the guild GGXrd"
#         self.assertEqual(message, expected)
#
#     def test_assigning_player_in_the_same_guild(self):
#         guild = Guild("GGXrd")
#         player = Player("Pesho", 90, 90)
#         guild.assign_player(player)
#         message = guild.assign_player(player)
#         expected = "Player Pesho is already in the guild."
#         self.assertEqual(message, expected)
#
#
# if __name__ == '__main__':
#     unittest.main()
#
