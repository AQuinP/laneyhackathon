import os
from openai import OpenAI

def talkToGPT(prompt):

    os.environ['OPENAI_API_KEY'] = "APIKEY" #REPLACE WITH API KEY

    client = OpenAI(api_key=os.environ['OPENAI_API_KEY']) #CREATES ENVIRONMENT VARIABLE FOR USER
    response = client.responses.create(
    model="gpt-4.1",
    input = prompt #WHAT GPT WILL BE PROMPTED WITH
    )

    print(response.output_text) #PRINT OUT GPT'S RESPONSE

def main():
    prompt = input("Type in your prompt: ") #PROMPT USER FOR INPUT
    talkToGPT(prompt) #SEND TO FUNCTION AS A PARAMETER SO USE FOR GPT

if __name__ == "__main__":
    main()