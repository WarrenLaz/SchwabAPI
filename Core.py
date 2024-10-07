import schwabdev
import dotenv
import os
import json
import time
dotenv.load_dotenv()

APIkey = os.getenv("APIk")
Secretkey = os.getenv("SECk")


client = schwabdev.Client(APIkey, Secretkey)
client.update_tokens_auto()
streamer = client.stream

streamer.start()

streamer.send(streamer.level_one_equities("SPY", "0,1,2,3,4,5"))
#parsed = client.quote("AMD").json()
#print(json.dumps(parsed, indent=4))

time.sleep(10)