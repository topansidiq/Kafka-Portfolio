import json

from confluent_kafka import Consumer  # type: ignore

consumer = Consumer(
    {
        "bootstrap.servers": "localhost:9092",
        "group.id": "temperature-monitor",
        "auto.offset.reset": "earliest",
    }
)

consumer.subscribe(["temperature"])

print("Waiting for sensor data...")

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            print("Consumer error:", msg.error())
            continue

        event = json.loads(msg.value().decode("utf-8"))

        print(
            f"Device: {event['device_id']} | "
            f"Sensor: {event['sensor']} | "
            f"Temperature: {event['temperature']} "
            f"{event['unit']}"
        )

except KeyboardInterrupt:
    print("Stopping consumer...")

finally:
    consumer.close()
