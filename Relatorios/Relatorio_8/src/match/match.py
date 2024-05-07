class Match:
    def __init__(self, match_id: str, players: list):
        self.match_id = match_id
        self.players = players

    def to_dict(self):
        player_ids = [player.id for player in self.players]
        return {"id": self.match_id, "players": player_ids}