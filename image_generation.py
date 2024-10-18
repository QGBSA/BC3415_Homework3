from openai import OpenAI
import os

def generate_image_from_prompt(prompt):
    openai_api = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=openai_api)
    
    response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
    )

    image_url = response.data[0].url

    return image_url
