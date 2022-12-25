from TextGenerator import stream_print
from TextGenerator import complete

class Town:

    def __init__(self, name, tournament=False, melee=False):
        self.character_count = 0

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
                 self.name + "\n"

        response = complete(prompt=prompt, \
                            max_tokens=512, \
                            temperature=1, \
                            stream=True)
        collected_events = []
        completion_text = ''
        self.character_count = 0

        for event in response:
            collected_events.append(event)
            event_text = event['choices'][0]['text']
            completion_text += event_text
            self.character_count = stream_print(event_text, \
                                                self.character_count)
        self.description = completion_text
        
        print("")
        prompt += self.description

        prompt += "\n"
        prompt += "There is a jousting tournament in town today. Describe the "
        prompt += "exciting atmosphere and the exciting faces of the festival"
        prompt += " goers.\n\n"

        response = complete(prompt=prompt, \
                            max_tokens = 256, \
                            temperature = 1, \
                            stream=True)
        collected_events = []
        completion_text = ''
        self.character_count = 0

        for event in response:
            collected_events.append(event)
            event_text = event['choices'][0]['text']
            completion_text += event_text
            self.character_count = stream_print(event_text, \
                                                self.character_count)
        return completion_text
        
    def generate_map(self):
        pass

