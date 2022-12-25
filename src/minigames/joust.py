import random

import openai
from dotenv import dotenv_values

from TextGenerator import complete
from TextGenerator import stream_print


config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

#engine_type = "text-ada-001"
engine_type = "text-davinci-003"


class Joust:

    def __init__(
        self,
        combatant_A_name="",
        combatant_B_name="",
    ):
        self.combatant_A_name = combatant_A_name
        self.combatant_B_name = combatant_B_name

    def main_joust(self):
        
        if self.combatant_A_name == "":
            self.combatant_A_name = self.generate_knight_name();
        if self.combatant_B_name == "":
            self.combatant_B_name = self.generate_knight_name();

        prompt = self.setup_joust(
            self.combatant_A_name,
            self.combatant_B_name,
        )

        print("We are gathered here to watch a joust between two brave " \
            + f"knights: {self.combatant_A_name}, and " \
            + f"{self.combatant_B_name}.\n Who will win on this perilous " \
            + "day? We shall soon find out!\n" \
        )

        while(True):
            user_input = self.get_joust_input(
                self.combatant_A_name,
                self.combatant_B_name,
            )

            if (user_input[0] == 0):
                winner_name = self.combatant_B_name
            elif (user_input[0] == 1):
                winner_name = self.combatant_A_name
            else:
                continue

            prompt += self.designate_joust_winner(winner_name, user_input)
            self.generate_joust(prompt)

            input("\n")

            break


    def designate_joust_winner(
        self,
        winner,
        details
    ):
        prompt = f"{winner} will win the joust by aiming " \
            + f"{details[1].lower()} because the opponent aimed " \
            + f"{details[2].lower()}."

        return prompt


    #this function returns a 1 if the player won, and a 0 if the computer won
    def get_joust_input(
        self,
        combatant_A_name="user",
        combatant_B_name="comp"
    ):
        possible_actions = ["high", "straight", "low"]
        user_action = input("Do you aim high, straight, or low?\n").lower()

        if user_action == "h":
            user_action = "high"
        elif user_action == "s":
            user_action = "straight"
        elif user_action == "l":
            user_action = "low"

        if user_action in possible_actions:
            print(f"{combatant_A_name} aims {user_action}.")
        else:
            user_action = random.choice(possible_actions)

            print(f"{combatant_A_name} can't decide, and picks randomly.\n" \
                + "The winds of fate decrees their lance will go " \
                + f"{user_action}!" \
            )

        possible_actions.remove(user_action)
        computer_action = random.choice(possible_actions)
        
        # Deprecated code? (commenting out so I don't remove something you 
        # want to keep for some unforseen reason).
        #
        #if user_action:
        #    pass
        #else:
        #    user_action = random.choice(possible_actions).capitalize()
        
        # Rock, paper, scissors
        #   high > straight
        #   low > high
        #   straight > low

        if all([
            user_action == "high",
            computer_action == "straight",
        ]):
            result = 1
        elif all([
            user_action == "straight",
            computer_action == "low",
        ]):
            result = 1
        elif all([
            user_action == "low",
            computer_action == "high",
        ]):
            result = 1
        else:
            result = 0

        return (result, user_action, computer_action)


    def setup_joust(
        self,
        knight_a,
        knight_b,
    ):
        
        if knight_a and knight_b:
            prompt = "Describe a joust between two knights named " \
                + f"{knight_a} and {knight_b}.\n\n"
        else:
            prompt = "Describe a joust between two nameless knights."

        return prompt


    def generate_joust(self, prompt):
        response = complete(
            prompt=prompt,
            max_tokens = 512,
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

            character_count = stream_print(
                event_text,
                character_count
            )

    def generate_knight_name(self):
        prompt = "Write the name of a knight who is partaking in a " \
            + "joust.\n\nHere are four good examples:\n\n" \
            + "Sir Arthilon, the blue and gold knight of Papilae\n" \
            + "Ser Bureaugard, the Brave\n" \
            + "Oxelot of the Golden Forest\n"

        response = complete(
            prompt=prompt,
            max_tokens = 16,
            temperature = 1,
        )

        return response.choices[0].text.strip()

