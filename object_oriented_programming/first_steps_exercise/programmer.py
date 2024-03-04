class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.skills = skills
        self.language = language
        self.name = name

    def watch_course(self, course_name: str, language: str, skills_earned: int):
        if language == self.language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        return f"{self.name} does not know {language}"

    def change_language(self, new_language: str, skills_needed: int):
        if skills_needed <= self.skills and new_language != self.language:
            previous_language = self.language
            self.language = new_language

            return f"{self.name} switched from {previous_language} to {new_language}"
        elif skills_needed <= self.skills and new_language == self.language:
            return f"{self.name} already knows {self.language}"
        return f"{self.name} needs {skills_needed - self.skills} more skills"

import unittest

class Tests(unittest.TestCase):
    def test_change_language_unsuccessful(self):
        programmer = Programmer("Lemmy", "Java", 100)
        res = programmer.change_language("Python", 150)
        self.assertEqual(res, "Lemmy needs 50 more skills")
        self.assertEqual(programmer.language, "Java")