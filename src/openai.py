from openai import OpenAI
from datetime import datetime
OPENAI_API_KEY = "<YOUR-API-KEY>"
client = OpenAI(api_key=OPENAI_API_KEY)

# model_name = ["gpt-3.5-turbo-0613", "gpt-4-1106-preview"]
def get_openai_response(model_name, max_tokens, user_prompt):
    response = client.chat.completions.create(
    model=model_name,
    messages=[
        {
        "role": "user",
        "content": user_prompt
        }
    ],
    temperature=1,
    max_tokens=max_tokens,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    current_datetime = datetime.now()
    timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    return response.choices[0].message.content, timestamp