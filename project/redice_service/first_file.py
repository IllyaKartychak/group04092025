import redis
import config

redis_client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    decode_responses=True,
    username=config.REDIS_USER,
    password=config.REDIS_PASSWORD,
)

for i in range(1000):
    message = input("Введіть повідомлення про події в школі на наступному тижні -> ")
    redis_client.publish("school", message)






