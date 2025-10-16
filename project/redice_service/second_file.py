import redis
import config

redis_client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    decode_responses=True,
    username=config.REDIS_USER,
    password=config.REDIS_PASSWORD,
)

pubsub = redis_client.pubsub()
pubsub.subscribe('school')

for message in pubsub.listen():
    string_message = str(message['data']).lower().strip()
    if "контрольна робота" in string_message:
        with open("message_info", 'a', encoding='utf-8') as infile:
            infile.write(string_message + "\n")
