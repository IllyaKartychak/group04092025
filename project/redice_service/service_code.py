"""Basic connection example.
"""

import redis
import config
import datetime as dt

redis_client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    decode_responses=True,
    username=config.REDIS_USER,
    password=config.REDIS_PASSWORD,
)

success = redis_client.set('foo', '12012')
# True

result = redis_client.get('foo')
print(result)
# >>> bar

# 5.1
# redis_client.set("Auto", "Toyota")
# 5.2
# redis_client.set("Pet", "Barsik", ex=7200)
# 5.3 and 5.4
# redis_client.lpush('list-product', 'flavour')
# redis_client.lpush('list-product', 'cookie')
# redis_client.rpush('list-product', 'choco')
# redis_client.expire('list-product', 7 * 24 * 60 * 60)
# 5.5
# redis_client.hset("ingredients", mapping={"flour": 250})
# redis_client.hset("ingredients", mapping={"milk": 500})
# redis_client.hset("ingredients", mapping={"sugar": 300})
# redis_client.hset("ingredients", mapping={"sugar": 300})

# redis_client.delete('ingredients')
