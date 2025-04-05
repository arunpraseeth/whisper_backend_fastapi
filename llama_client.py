import requests

def generate_reply(prompt):
    response = requests.post("http://192.168.2.38/v1/chat/completions", json={
        "model": "meta-llama-3-8b-instruct",
        "messages": [
            {"role": "user", "content": prompt},
          ],
        "temperature": 0.7,
        "max_tokens": 300,
    })
    return response.json()['choices'][0]['message']['content']
