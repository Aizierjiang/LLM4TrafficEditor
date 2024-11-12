import openai
import config as config


def call(prompt=config.base_prompt, model=config.model):
    openai.api_key = config.api_key
    response = openai.Completion.create(model=model, prompt=prompt, max_tokens=20, temperature=0)
    usable_response = response['choices'][0]['text'].strip()
    return usable_response
