import json
from os import environ

# pip install openai
import openai

openai.api_key = environ.get("OPENAI_API_KEY")
openai.api_base = "http://openai.plms.ai/v1"
# openai.api_base = "http://34.195.96.131/v1"

def get_gpt_response(prompt: str):
    """

    Args:
        prompt: the prompt to ask the gpt3.5

    Returns:
        the response from the gpt3.5

    """
    messages = [{"role": "user", "content": prompt}]
    model = "gpt-3.5-turbo"  # or gpt-4
    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].message.content
    return response


if __name__ == "__main__":
    prompt = "Who are you?"
    response = get_gpt_response(prompt)
    print(response)
