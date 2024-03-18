from database import Database
from pokedex import Pokedex
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
# db.resetDatabase()

pokedex = Pokedex(db)

pokedex.get_pokemons_have_evolution()
pokedex.get_pokemon_by_name("Pikachu")
pokedex.get_pokemons_by_type(["Poison", "Fighting"])
pokedex.get_pokemons_just_one_weakness("water")
pokedex.get_pokemons_avg_spawns_less_two()
