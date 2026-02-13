import base64
from groq import Groq

def describe_image(image_path, api_key):
    client = Groq(api_key=api_key)

    with open(image_path, "rb") as img:
        image_bytes = img.read()

    b64 = base64.b64encode(image_bytes).decode("utf-8")

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this image clearly."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{b64}"
                        }
                    }
                ]
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print("Vision RAG System")
