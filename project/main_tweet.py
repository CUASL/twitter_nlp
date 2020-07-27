import twythonx
import time

api = twythonx.twit()

i = 7

while True:
    msg = f"Hello Wordl! {i}"+" #cuasl"
    print(msg)
    api.post(msg)
    time.sleep(10)
    i+=1