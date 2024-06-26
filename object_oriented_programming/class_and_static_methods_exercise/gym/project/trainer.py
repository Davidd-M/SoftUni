from project.get_next_id_mixin import GetNextId


class Trainer(GetNextId):
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

