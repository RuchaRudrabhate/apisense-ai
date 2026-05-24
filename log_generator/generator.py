import random
import json
import pandas as pd 

from services import SERVICES
from utils import (
    generate_trace_id,
    generate_status_code,
    generate_severity,
    generate_error_message,
    generate_latency,
    generate_timestamp
)

LOG_COUNT = 500
logs = []

for _ in range(LOG_COUNT):
    service = random.choice(list(SERVICES.keys()))
    endpoint = random.choice(SERVICES[service])

    status_code = generate_status_code()
    log = {
        "timestamp": generate_timestamp(),
        "trace_id": generate_trace_id(),
        "service": service,
        "endpoint": endpoint,
        "method": random.choice(["GET", "POST"]),
        "status_code": status_code,
        "latency_ms": generate_latency(status_code),
        "severity": generate_severity(status_code),
        "error_message": generate_error_message(status_code),
        "host": f"{service}-pod-{random.randint(1, 5)}",
        "region": random.choice([
            "ap-south-1",
            "us-east-1",
            "eu-west-1"
        ])
    }

    logs.append(log)


#Save logs as JSON
with open("datasets/logs.json","w") as file:
    json.dump(logs,file,indent=4)

#Export as CSV
df = pd.DataFrame(logs)
df.to_csv("datasets/logs.csv",index=False)

print("Logs generated successfully.")