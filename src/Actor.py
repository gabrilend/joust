from TextGenerator import complete

class Actor:

    def __init__(self, name, description, title, active=None, passive="having an existential crisis", pronoun, possessive):
        self.name = name
        self.description = description
        self.title = title
        self.active = active
        self.passive = passive
        self.pronoun = pronoun
        self.possessive = possessive

    def setActive(self, active):
        self.active = active

    def describe(self):
        return complete(prompt=description,
                        max_tokens=256,
                        temperature=1)

    def describeActivity(self):
        if active != None:
            activity = active
            adverb = ""
        else:
            activity = passive
            adverb = "idly "
        return complete(prompt="Write a description of " + self.name + " " + self.title + " " + adverb + activity + ".",
                        max_tokens=256,
                        temperature=1)