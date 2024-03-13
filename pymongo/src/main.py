from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017', )

db = client['countries']

paises = db.countries

# Inserindo um documento
results = paises.insert_one({
    'name': 'Brasil',
    'temp':{
        'SP': 26,
        'RJ': 32,
        'MG': 26
    }
})

# Verificando se o documento foi inserido
if results.acknowledged:
    print('Documento adicionado!')
else:
    print('Erro')

# Fazendo update em um documento
results = paises.update_one(
    {'temp.MG':{'$exists':True}},
    {'$set':{'temp.MG':30}}
)

if results.acknowledged:
    print('Documento atualizado!')
else:
    print('Erro')

# Removendo um documento e fazendo a verificação se foi removido
results = paises.delete_one({'name':'Brasil'})
if results.acknowledged:
    print('Documento removido!')
else:
    print('Erro')

# Buscando um documento com nome igual a Brasil
results = paises.find({'name':'Brasil'})

# Imprimindo o resultado da pesquisa
for result in results:
    print(result)