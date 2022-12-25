from TextGenerator import complete

class Actor:

    def __init__(
        self,
        name,
        description,
        title,
        pronoun,
        possessive,
        active=None,
        passive="having an existential crisis"
    ):
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
        return complete(
            prompt=description,
            max_tokens=256,
            temperature=1
        )

    def describeActivity(self):
        if active != None:
            activity = active
            adverb = ""
        else:
            activity = passive
            adverb = "idly "
        
        prompt = f"Write a description of {self.name} " \
            + f"{self.title} {adverb} {activity}."

        return complete(
            prompt=prompt,
            max_tokens=256,
            temperature=1
        )

