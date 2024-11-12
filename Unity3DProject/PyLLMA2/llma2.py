import PyLLMA2.llma2 as llma2
import config as config

def call(prompt=config.base_prompt):
    response = llma2.call(prompt)  # Call LLMA2 API with the prompt
    usable_response = response.strip()  # Strip any leading/trailing whitespace
    return usable_response