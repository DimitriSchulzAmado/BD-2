from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json


cloud_config= {
  'secure_connect_bundle': 'secure-connect-dbiot.zip'
}

with open("dbiot-token.json") as f:
    secrets = json.load(f)

CLIENT_ID = secrets["clientId"]
CLIENT_SECRET = secrets["secret"]

auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

session.set_keyspace('dbiot')

session.execute("""
    CREATE TABLE IF NOT EXISTS peca (
        id_peca INT PRIMARY KEY,
        nome TEXT,
        carro TEXT,
        estante INT,
        nivel INT,
        quantidade INT
    );
""")

result = session.execute(
    'BEGIN BATCH '+
    "INSERT INTO peca(id_peca,nome,carro,estante,nivel,quantidade) VALUES(5, 'Pistao', 'Mustang', 4, 1, 167);"+
    "INSERT INTO peca(id_peca,nome,carro,estante,nivel,quantidade) VALUES(4, 'Suspencao', 'Argo', 1, 1, 3500);"+
    'APPLY BATCH;'
)

person_input = input("Digite o carro: ")

    
result = session.execute(f"""
    SELECT 
        nome,
        estante, 
        quantidade
    FROM peca
    WHERE 
        carro = '{person_input}'
    ALLOW FILTERING;                    
""").all()


if result is not None:
    print(result)

cluster.shutdown()
