import redis
redis_conn = redis.Redis(
    host='localhost',
    port=6379,
    username='root',
    db=0
    )

# Adiciona um valor a chave
redis_conn.set('foo', 'Teste')

# Deleta a chave
redis.delete('foo')

# Adiciona um campo e valor ao hash
redis_conn.hset("product:1", mapping={
    "name": "Smartphone X",
    "price": 100.0,
    "brand": "Techtech",
    "description": "An generic Smartphone",
})

# Retorna um dicionário com todos os campos e valores do hash
redis_conn.hgetall("product:1")

# Adiciona um valor a lista
redis_conn.lpush("product:1", 10)

# Tamanho da lista
inventory_len = redis_conn.llen("product:1")

redis_conn.expire("product:1", 60) # Expira a chave em 60 segundos
redis_conn.ttl("product:1") # Retorna o tempo restante para a chave expirar