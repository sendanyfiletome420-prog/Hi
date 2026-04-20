import chainlit as cl
import requests

API_URL = "https://goodhunter421-poemcap.hf.space/generate"

@cl.on_message
async def main(message: cl.Message):
    try:
        response = requests.post(
            API_URL,
            json={"text": message.content},
            timeout=60
        )
        result = response.json()
        output = result.get("response", "No response from model")

    except Exception as e:
        output = f"Error: {str(e)}"

    await cl.Message(content=output).send()
