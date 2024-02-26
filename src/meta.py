import os
import replicate
from datetime import datetime
os.environ["REPLICATE_API_TOKEN"] = "<YOUR-API-TOKEN>"

# model: llama-2-70b-chat
def get_meta_response(user_prompt, max_length):
    event = ''
    res = ''
    for event in replicate.stream(
    "meta/llama-2-70b-chat",
    input={
        "debug": False,
        #"top_k": 1,
        "top_p": 1,
        "prompt": user_prompt,
        "max_length": max_length,
        "temperature": 1,
        "system_prompt": "",
        "max_new_tokens": 500,
        "min_new_tokens": -1,
        "repetition_penalty": 1.15
    },
    ):
        res += str(event)

    res = str(res)
        
    current_datetime = datetime.now()
    timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S") 

    return res, timestamp
