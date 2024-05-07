from neo4j import Driver

from src.player.player import Player


class PlayerController:
    node_name = "PLAYER"

    def __init__(self, driver: Driver):
        self.driver = driver

    def execute_query(self, query, params):
        with self.driver.session() as session:
            return session.run(query, params)

    def create(self, player: Player):
        self.execute_query("CREATE(:<node_name>, {name: $name, id: $id})", player.to_dict())

    def update(self, player: Player):
        self.execute_query(
            "MATCH(p:<node_name> {id: $id}) SET p.name = $name",
            player.to_dict(),
        )

    def delete(self, player_id: str):
        self.execute_query(
            "MATCH(p:<node_name> {id: $id}) DELETE p",
            {"id": player_id},
        )

    def get(self, player_id: str):
        return self.execute_query(
            "MATCH(p:<node_name> {id: $id}) RETURN p",
            {"id": player_id},
        )

    def list(self):
        return self.execute_query(
            "MATCH(p:<node_name> {}) RETURN p",
            {}
        )
