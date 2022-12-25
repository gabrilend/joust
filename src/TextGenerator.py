import openai

def complete(self, engine_type="text-davinci-003", prompt, max_tokens, stream=False):
    return openai.Completion.create(self.engine_type, prompt, max_tokens, stream)