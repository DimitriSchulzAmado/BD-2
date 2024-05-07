import uuid
from neo4j import GraphDatabase
from src.match.match import Match
from src.match.match_controller import MatchController
from src.player.player import Player
from src.player.player_controller import PlayerController

NEO4J_URL = 'neo4j://localhost:7474'
driver = GraphDatabase.driver(NEO4J_URL, auth=('neo4j', 'dockeradmin'), max_connection_lifetime=1000)

player_controller = PlayerController(driver)
match_controller = MatchController(driver)

player = Player(
    name="JUSTINO",
    _id=str(uuid.uuid4())
)
player_controller.create(player)


match = Match(_id=str(uuid.uuid4()), players=[player])
match_controller.create(match)

# Buscando informações sobre a partida do jogador
player_id = player.to_dict()["id"]
print(match_controller.get_by_player(player_id))

# Fechando a conexão com o banco de dados
driver.close()
