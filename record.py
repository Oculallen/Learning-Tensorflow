import requests
import json
from datetime import datetime
import time

def record():
    recording = []
    print("Recording until any key pressed")
    try:
        while True:
            response = requests.get(f'http://{path}:6721/session')
            time.sleep(0.5)
            print("Done")
            data = response.json()
            print(data["sessionip"])
            recording.append(response.json())
    except KeyboardInterrupt:
        print("Recording Finished")
        return recording

path = input("Please enter the echo ip")

with open(f'recording.json', 'w') as f:
    rec = record()
    json.dump(rec, f)
    f.close()

print(f'file saved as recording{datetime.date()}.json in local directory')
