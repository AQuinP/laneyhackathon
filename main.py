import openai
import os
from openai import OpenAI

def talkToGPT(prompt):

    os.environ['OPENAI_API_KEY'] = "APIKEY"

    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    response = client.responses.create(
    model="gpt-4.1",
    input = prompt
    )

    print(response.output_text)

def main():
    prompt = input("Type in your prompt: ")
    talkToGPT(prompt)

if __name__ == "__main__":
    main()