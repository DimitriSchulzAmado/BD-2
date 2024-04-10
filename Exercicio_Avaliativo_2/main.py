'''
CREATE(:Person:Pawn{name:'Rogério', gender:'M', age: 47})
CREATE(:Person:Engineer{name:'André', gender:'M', age: 43})
CREATE(:Person:Attorney{name:'Beatriz', gender:'F', age: 25})
CREATE(:Person:Doctor{name:'Juliana', gender:'F', age: 27})
CREATE(:Person:Doctor{name:'Mariana', gender:'F', age: 27})

CREATE(:Person:Businessperson:Retiree{name:'Alexandre', gender:'M', age: 57})
CREATE(:Person:Businessperson:Housewife{name:'Christina', gender:'F', age: 53})
CREATE(:Person:Engineer:Technician{name:'Dimitri', gender:'M', age: 21})
CREATE(:Person:Psychologist:Fortuneteller{name:'Ana Julia', gender:'F', age: 22})
CREATE(:Animal:Dog{name:'Luna', gender:'F', age: 3})

MATCH(p:Person{name: 'Dimitri'}),(n:Animal:Dog{name:'Luna'})
CREATE(p)-[:HAS_PET{since:'2021'}]->(n)

MATCH(p:Person{name: 'Alexandre'}),(n:Person{name:'Christina'})
CREATE(n)-[:MARRIED_WITH{since:'2003'}]->(p),(n)<-[:MARRIED_WITH{since:'2003'}]-(p)

MATCH(p:Person{name: 'Dimitri'}),(n:Person{name:'Ana Julia'})
CREATE(n)-[:DATES_WITH{since:'2024'}]->(p),(n)<-[:DATES_WITH{since:'2024'}]-(p)

MATCH(p:Person{name: 'Dimitri'}),(n:Person{name:'Christina'})
CREATE(n)-[:IS_PARENT_OF]->(p)

MATCH(p:Person{name: 'Dimitri'}),(n:Person{name:'Alexandre'})
CREATE(n)-[:IS_PARENT_OF]->(p)

MATCH(p:Person{name: 'Beatriz'}),(n:Person{name:'Mariana'})
CREATE(n)-[:COUSIN_OF]->(p),(n)<-[:COUSIN_OF]-(p)

MATCH(p:Person{name: 'Juliana'}),(n:Person{name:'Mariana'})
CREATE(n)-[:BROTHER_OF]->(p),(n)<-[:BROTHER_OF]-(p)

MATCH(p:Person{name: 'Dimitri'}),(n:Person{name:'Beatriz'})
CREATE(n)-[:COUSIN_OF]->(p),(n)<-[:COUSIN_OF]-(p)

MATCH(p:Person{name: 'Dimitri'}),(n:Person{name:'Rogério'})
CREATE(n)-[:UNCLE_OF]->(p),(n)<-[:NEPHEW_OF]-(p)

MATCH(p:Person{name: 'Dimitri'}),(n:Person{name:'André'})
CREATE(n)-[:UNCLE_OF]->(p),(n)<-[:NEPHEW_OF]-(p)
'''

from neo4j import GraphDatabase

def find_engineers(db):
    query = "MATCH (p:Person:Engineer) RETURN p.name"
    with db.session() as session:
        result = session.run(query)

        for record in result:
            print(f"{record['p.name']} é engenheiro(a)")


def find_parents_of(db, child_name):
    query = f"MATCH (p:Person)-[:IS_PARENT_OF]->(c:Person {{name: '{child_name}'}}) RETURN p.name"
    with db.session() as session:
        result = session.run(query)

        for record in result:
            print(f"{record['p.name']} é pai/mãe de {child_name}")


def find_pets_of_family(db):
    query = "MATCH (p:Person)-[:HAS_PET]->(pet) RETURN p.name, pet.name"
    with db.session() as session:
        result = session.run(query)

        for record in result:
            print(f"{record['p.name']} tem um animal de estimação chamado {record['pet.name']}")


def main():
    title = "Exercício NEO4J"
    separator = "=" * 10
    top_bottom_separator = "=" * len(title)

    print(top_bottom_separator)
    print(f"{separator}{title}{separator}")
    print(top_bottom_separator)

    print("1. Quem é engenheiro?")
    print("2. Quem é pai de quem?")
    print("3. Desde quando está namorando?")
    print("4. Sair")
    
    loop = True
    while loop:
        option = input("Escolha uma das opções: ")

        match int(option):
            case 5:
                loop = False
            case 1:
                find_engineers(neo4j)
            case 2:
                name = input("Insira o nome da pessoa: ")
                find_children_of(neo4j, name)
            case 3:
                name = input("Insira o nome da pessoa: ")
                find_partner_since(neo4j, name)

    neo4j.close()
    

if __name__ == "__main__":
    uri = "neo4j+s://629ae45d.databases.neo4j.io"
    user = "neo4j"
    password = "3ZsZtTP-cPZi23Dvhg_S_lCJIhK6VLnk9sCm_Xy8RzU"

    driver = GraphDatabase.driver(uri, auth=(user, password))
    
    main(driver)

    driver.close()
