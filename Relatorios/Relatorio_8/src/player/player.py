class Player:
    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id

    def to_dict(self, exclude: list[str] = None):
        player_dict = {
            'name': self.name,
            'id': self.id
        }

        if exclude is not None:
            for key in exclude:
                if key in player_dict:
                    del player_dict[key]

        return player_dict
