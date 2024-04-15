class GetNextId:
    id = 0  # to avoid warning

    @classmethod
    def get_next_id(cls):
        cls.id += 1
        return cls.id - 1
