from fastapi import FastAPI, File, Form, UploadFile
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
import base64
from typing import Any, cast

load_dotenv()

app = FastAPI()
client = OpenAI()


class Request(BaseModel):
    message: str


@app.get("/")
def root():
    return {"msg": "Test"}


# this is only a test endpoint
@app.post("/gpt-response")
def gpt_response(request_body: Request):
    response = client.responses.create(model="gpt-5-nano", input=request_body.message)
    return response.output_text


# /POST form-data
@app.post("/review-image")
async def review_image(image: UploadFile = File(...)):
    content = await image.read()
    b64_image = base64.b64encode(content).decode("utf-8")
    prompt = "Please describe this image"
    mime_type = image.content_type or "image/jpeg"

    payload = [
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": prompt},
                {
                    "type": "input_image",
                    "image_url": f"data:{mime_type};base64,{b64_image}",
                },
            ],
        }
    ]

    try:
        response = client.responses.create(model="gpt-5-nano", input=cast(Any, payload))
        return {"message": response.output_text}
    except Exception as e:
        return {"error": e}
