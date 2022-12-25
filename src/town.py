import openai
from dotenv import dotenv_values

from TextGenerator import stream_print
from TextGenerator import complete


config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


class Town:

    def __init__(
        self,
        name,
        tournament=False,
        melee=False
    ):

        self.name = name
        self.tournament = tournament
        self.melee = melee
        self.description=""
            
    def __str__(self):
        return self.name

    def describe_town(self, person_name=""):
        if self.description != "":
            print(self.description)
        else:
            self.generate_and_stream_description()

    def generate_and_stream_description(self):
        
        prompt = "Describe the town square of a medieval city named " + \
            f"{self.name}.\n"

        response = complete(
            prompt=prompt,
            max_tokens=512,
            temperature=1,
            stream=True,
        )

        collected_events = []
        completion_text = ''
        character_count = 0

        for event in response:
            collected_events.append(event)
            event_text = event['choices'][0]['text']
            completion_text += event_text

            character_count = stream_print(
                event_text,
                character_count,
            )

        self.description = completion_text
        
        print("")
        prompt = f"{self.description}\nThere is a jousting tournament in " \
            + "town today. Describe the exciting atmosphere and the " \
            + "excited faces of the festival goers.\n\n"

        response = complete(
            prompt=prompt,
            max_tokens = 256,
            temperature = 1,
            stream=True,
        )

        collected_events = []
        completion_text = ''
        character_count = 0

        for event in response:
            collected_events.append(event)
            event_text = event['choices'][0]['text']
            completion_text += event_text
            character_count = stream_print(event_text, character_count)

        return completion_text
        
    def generate_map(self):
        pass

