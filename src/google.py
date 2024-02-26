import google.generativeai as genai
from datetime import datetime

genai.configure(api_key="<YOUR-API-KEY>")

# Gemini Pro (gemini-1.0-pro-001)
def get_google_response(user_prompt, max_tokens):
    # Set up the model
    generation_config = {
        "temperature": 1,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": max_tokens,
    }

    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
    ]

    model = genai.GenerativeModel(
        model_name="gemini-1.0-pro-001",
        generation_config=generation_config,
        safety_settings=safety_settings,
    )

    response = model.generate_content(user_prompt)

    current_datetime = datetime.now()
    timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    try:
        return response.text, timestamp
    except ValueError:
        print(response.prompt_feedback)
        return str(response.prompt_feedback), timestamp


# PaLM 2 (text-bison-001)
def get_palm2_response(user_prompt, max_tokens):

    defaults = {
        "model": "models/text-bison-001",
        "temperature": 1,
        "candidate_count": 1,
        "top_k": 1,
        "top_p": 1,
        "max_output_tokens": max_tokens,
        "stop_sequences": [],
        "safety_settings": [
            {"category": "HARM_CATEGORY_DEROGATORY", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_TOXICITY", "threshold": "BLOCK_NONE"},
            {
                "category": "HARM_CATEGORY_VIOLENCE",
                "threshold": "BLOCK_NONE",
            },
            {"category": "HARM_CATEGORY_SEXUAL", "threshold": "BLOCK_NONE"},
            {
                "category": "HARM_CATEGORY_MEDICAL",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS",
                "threshold": "BLOCK_NONE",
            },
        ],
    }

    prompt = user_prompt

    response = genai.generate_text(**defaults, prompt=prompt)

    current_datetime = datetime.now()
    timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    try:
        return response.result, timestamp
    except ValueError:
        print(response.prompt_feedback)
        return str(response.prompt_feedback), timestamp

