class Pokedex:
    def __init__(self, db):
        self.db = db

    pokemons = db.collection.find()
    
    def getPokemonByName(name: str):
        return db.collection.find({"name": name})
    
    def getPokemonsByType(types: list):
        return db.collection.find({"type": {"$in": types}})
    
    