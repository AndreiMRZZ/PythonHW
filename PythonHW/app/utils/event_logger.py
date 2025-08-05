import pika
import json
import time
MAX_RETRIES = 10

for attempt in range(MAX_RETRIES):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
        channel = connection.channel()
        channel.queue_declare(queue='log_queue', durable=True)
        break
    except pika.exceptions.AMQPConnectionError:
        print(f"[LOG] RabbitMQ not ready, retrying ({attempt + 1}/{MAX_RETRIES})...")
        time.sleep(2)
else:
    raise Exception("Could not connect to RabbitMQ after multiple attempts.")

def send_log(event_type: str, data: dict):
    msg = {
        "type": event_type,
        "data": data
    }

    #serializare cu json si trimitere mesaj
    channel.basic_publish(
        exchange='',
        routing_key='log_queue',
        body= json.dumps(msg),
        properties= pika.BasicProperties(
            delivery_mode= 2
        )
    )