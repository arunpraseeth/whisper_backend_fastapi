import requests

def generate_reply(prompt, clientUrl):
    response = requests.post(clientUrl, json={
        "model": "meta-llama-3-8b-instruct",
        "messages": [
            {"role": "user", "content": prompt},
          ],
        "temperature": 0.7,
        "max_tokens": 300,
    })
    return response.json()['choices'][0]['message']['content']
