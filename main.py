import openai
import requests

openai.api_key = "YOUR_API_KEY"

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

prompt = "What is the meaning of life?"
response = generate_text(prompt)
print(response)
