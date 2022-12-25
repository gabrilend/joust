import array

from TextGenerator import complete
from TextGenerator import stream_print


class Location:

    def __init__(
        self,
        name="",
        description="",
        actors=[],
        adjacentPlaces=[]
    ):
        self.name = name
        self.description = description
        self.actors = actors
        self.adjacentPlaces = adjacentPlaces
        self.prompt = f"Describe a {self.name} in a few sentences. Focus " \
            + "on the details, and use romantic language. Think about how " \
            + "it feels to be in that space and describe it as if seen for " \
            + "the first time."


    def __str__(self):
        return self.description

    def move_to(self, actor):
        if actor not in self.actors:
            self.actors += actor
        actor.location = self
    
    def describe(self, stream=True):
        if self.name == "":
            self.generate_name()

        if stream:
            return self.__generate_and_stream_description()
        else:
            self.description = __generate_description
            return self.description
   
    def __generate_description(self):
        # DRY!
        prompt = self.prompt
        # prompt = f"Describe a {self.name} in a few sentences. Focus on " + \
        #     "the details, and use romantic language. Think about how it " + \
        #     "feels to be in that space and describe it as if seen for " + \
        #     "the first time."

        if not self.actors:
            prompt += f"\n\nThere is nobody here."
        
        i = 0
        while i <= len(self.actors):
            prompt += f"\n{self.actors[i]} is here."
            i += 1

        response = complete(
            prompt=prompt,
            max_tokens = 256,
            temperature = 1,
            stream=False,
        )

        return self.description

    def __generate_and_stream_description(self):
        # DRY!
        prompt = self.prompt
        # prompt = f"Describe a {self.name} in a few sentences. Focus on " + \
        #     "the details, and use romantic language. Think about how it " + \
        #     "feels to be in that space and describe it as if seen for " + \
        #     "the first time."

        if len(self.actors) == 0:
            prompt += f"\n\nThere is nobody here."
        
        i = 0
        while(i < len(self.actors)):
            prompt += f"\n{self.actors[i]} is here."
            i += 1

        response = complete(
            prompt=prompt,
            max_tokens = 256,
            temperature = 1,
            stream=True
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
                character_count
            )

        self.description = response

        return self.description

    def generate_name(self):
        prompt = "Write the name of a town from a fantasy medieval world." \
            + "\n\nHere are four good examples:" \
            + "\nSorenthal, Keep of the West" \
            + "\nGaridsbridge, the Town by the Water" \
            + "\nSarenbrook\n"

        response = complete(
            prompt=prompt,
            max_tokens = 16,
            temperature = 1
        )

        self.name = response.choices[0].text.strip()

        return self.name

