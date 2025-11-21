from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

app = FastAPI()
client = OpenAI()


class Request(BaseModel):
    message: str


@app.get("/")
def root():
    return {"msg": "Test"}


@app.post("/gpt-response")
def gpt_response(request_body: Request):
    response = client.responses.create(model="gpt-5-nano", input=request_body.message)
    return response.output_text
