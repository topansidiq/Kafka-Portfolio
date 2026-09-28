import json
import random
import time
from datetime import datetime, timezone

from confluent_kafka import Producer  # pyright: ignore[reportMissingImports]

producer = Producer({"bootstrap.servers": "localhost:9092"})


def delivery_report(err, msg):
    if err:
        print(f"Delivery failed: {err}")
    else:
        print(f"Delivered: {msg.topic()} [{msg.partition()}] offset={msg.offset()}")


try:
    while True:
        temperature = round(random.uniform(30.0, 40.0), 2)

        event = {
            "device_id": "PLC-001",
            "sensor": "AI-04",
            "temperature": temperature,
            "unit": "C",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        producer.produce(
            topic="temperature",
            key=event["device_id"],
            value=json.dumps(event),
            callback=delivery_report,
        )

        producer.poll(0)
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping producer...")

finally:
    producer.flush()
