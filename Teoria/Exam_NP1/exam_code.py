# CREATE (:Mundo {name: 'Terra dos Dragões'})
# CREATE (:Mundo {name: 'Terra dos Elfos'})
# CREATE (:Pagina {titulo: 'História da Terra dos Dragões'})
# CREATE (:Pagina {titulo: 'História da Terra dos Elfos'})
# CREATE (:Personagem {name: 'John Doe'})
# CREATE (:Personagem {name: 'Jane Doe'})

# MATCH (c:Character {nome: 'John Doe'})-[:CONTAINS]->(p:Pagina) RETURN p.titulo, p.descricao

# MATCH (m:Mundo {name: 'Terra dos Elfos'})-[:CONTAINS]->(c:Character) RETURN c.name ORDER BY c.creation_date

# MATCH (m:Mundo {name: 'Terra dos Elfos'})-[:CONTAINS]->(c:Character) WHERE c.cultura = 'Marruchi' OR c.cultura = 'Yuni' OR c.profissao = 'Caçador' OR c.profissao = 'Canalizador' CREATE (m)-[:CONTAINS]->(:Pagina {titulo: 'História da Terra dos Elfos'})

from neo4j import GraphDatabase

# Connect to the Neo4j database
uri = "bolt://localhost:7687"
username = "neo4j"
password = "password"
driver = GraphDatabase.driver(uri, auth=(username, password))

# Create a session to execute queries
with driver.session() as session:
    # Create Mundo nodes
    session.run("CREATE (:Mundo {name: 'Terra dos Dragões'})")
    session.run("CREATE (:Mundo {name: 'Terra dos Elfos'})")

    # Create Pagina nodes
    session.run("CREATE (:Pagina {titulo: 'História da Terra dos Dragões'})")
    session.run("CREATE (:Pagina {titulo: 'História da Terra dos Elfos'})")

    # Create Personagem nodes
    session.run("CREATE (:Personagem {name: 'John Doe'})")
    session.run("CREATE (:Personagem {name: 'Jane Doe'})")

    # Query 1: Retrieve the titles and descriptions of pages connected to John Doe
    result = session.run("MATCH (c:Personagem {name: 'John Doe'})-[:CONTAINS]->(p:Pagina) RETURN p.titulo, p.descricao")
    for record in result:
        print(record["p.titulo"], record["p.descricao"])

    # Query 2: Retrieve the names of characters connected to the Mundo 'Terra dos Elfos' ordered by creation date
    result = session.run("MATCH (m:Mundo {name: 'Terra dos Elfos'})-[:CONTAINS]->(c:Personagem) RETURN c.name ORDER BY c.creation_date")
    for record in result:
        print(record["c.name"])

    # Query 3: Create a new page 'História da Terra dos Elfos' connected to Mundo 'Terra dos Elfos'
    session.run("MATCH (m:Mundo {name: 'Terra dos Elfos'})-[:CONTAINS]->(c:Personagem) WHERE c.cultura = 'Marruchi' OR c.cultura = 'Yuni' OR c.profissao = 'Caçador' OR c.profissao = 'Canalizador' CREATE (m)-[:CONTAINS]->(:Pagina {titulo: 'História da Terra dos Elfos'})")

# Close the driver connection
driver.close()


