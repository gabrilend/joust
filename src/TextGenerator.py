import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

def complete(engine_type="text-davinci-003", \
             prompt="", \
             max_tokens=128, \
             temperature=0.7, \
             stream=False):

    return openai.Completion.create(engine=engine_type, \
                                    prompt=prompt, \
                                    max_tokens=max_tokens, \
                                    temperature=temperature, \
                                    stream=stream)

def stream_print(text, character_count):
    character_count += len(text)
    if character_count >= 80:
        if text[0] != " " and text[0] != "\n":
            print("-\n-", end="", sep="", flush=True)
        else:
            print("\n", end="", sep="", flush=True)
        character_count = len(text)
    else:
        if "\n" in text:
            character_count = len(text)
    print(text, end="", sep="", flush=True)
    return character_count

