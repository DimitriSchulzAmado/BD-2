from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def get_teacher_by_name(self, name):
        query = (
            "MATCH (t:Teacher {name: $name}) "
            "RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        )
        with self.driver.session() as session:
            result = session.run(query, name=name)
            return result.single()

    def get_teachers_by_name_starting_with(self, letter):
        query = (
            "MATCH (t:Teacher) "
            "WHERE t.name STARTS WITH $letter "
            "RETURN t.name AS name, t.cpf AS cpf"
        )
        with self.driver.session() as session:
            result = session.run(query, letter=letter)
            return list(result)

    def get_all_city_names(self):
        query = (
            "MATCH (c:City) "
            "RETURN c.name AS name"
        )
        with self.driver.session() as session:
            result = session.run(query)
            return [record["name"] for record in result]

    def get_schools_with_number_range(self, min_number, max_number):
        query = (
            "MATCH (s:School) "
            "WHERE s.number >= $min_number AND s.number <= $max_number "
            "RETURN s.name AS name, s.address AS address, s.number AS number"
        )
        with self.driver.session() as session:
            result = session.run(query, min_number=min_number, max_number=max_number)
            return list(result)
    
    def get_oldest_and_youngest_teacher(self):
        query = (
            "MATCH (t:Teacher) "
            "RETURN min(t.ano_nasc) AS mais_velho, max(t.ano_nasc) AS mais_jovem"
        )
        with self.driver.session() as session:
            result = session.run(query)
            return result.single()

    def get_average_population(self):
        query = (
            "MATCH (c:City) "
            "RETURN avg(c.population) AS media_populacao"
        )
        with self.driver.session() as session:
            result = session.run(query)
            return result.single()

    def get_city_by_cep(self, cep):
        query = (
            "MATCH (c:City {cep: $cep}) "
            "RETURN replace(c.name, 'a', 'A') AS name"
        )
        with self.driver.session() as session:
            result = session.run(query, cep=cep)
            return result.single()

    def get_third_char_of_teacher_names(self):
        query = (
            "MATCH (t:Teacher) "
            "RETURN substring(t.name, 2, 1) AS char"
        )
        with self.driver.session() as session:
            result = session.run(query)
            return list(result)
        
    # Question 3 - Teacher CRUD
    def execute_write(self, query, parameters=None):
        with self.driver.session() as session:
            session.write_transaction(lambda tx: tx.run(query, parameters))

    def execute_read(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.read_transaction(lambda tx: tx.run(query, parameters))
            return result.single()
