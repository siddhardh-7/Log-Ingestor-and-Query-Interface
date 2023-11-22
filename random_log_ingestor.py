import requests
import json
import random
import string
import datetime

# from django.utils.timezone import utc

url = "http://localhost:3000/ingest/"

levels = [
    "error",
    "trace",
    "info",
    "warning",
    "fatal",
]


# Function to generate random data
def generate_random_data():
    data = {
        "level": levels[random.randint(0, 4)],
        "message": "The message is: "
        + "".join(random.choices(string.ascii_letters + string.digits, k=15)),
        "resourceId": "server-"
        + "".join(random.choices(string.ascii_letters + string.digits, k=4)),
        "timestamp": (datetime.datetime.now()).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "traceId": "".join(random.choices(string.ascii_letters + string.digits, k=5)),
        "spanId": "span-"
        + "".join(random.choices(string.ascii_letters + string.digits, k=3)),
        "commit": "".join(random.choices(string.ascii_letters + string.digits, k=7)),
        "parentResourceId": "".join(
            random.choices(string.ascii_letters + string.digits, k=8)
        ),
    }
    # print(
    #     f"{data['level']=}\n {data['message']=}\n {data['resourceId']=}\n {data['timestamp']=}\n {data['traceId']=}\n {data['spanId']=}\n "
    # )
    return data


# Number of times to run the command
n = 12

for _ in range(n):
    # Generate random data
    random_data = generate_random_data()
    print(random_data)
    # Send the request
    response = requests.post(
        url, headers={"Content-Type": "application/json"}, data=json.dumps(random_data)
    )

    # Print the response
    print(response.text)
