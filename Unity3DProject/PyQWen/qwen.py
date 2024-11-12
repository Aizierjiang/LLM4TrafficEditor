import PyQWen.qwen as qwen  # Adjusted for QWen
import config as config

def call(prompt=config.base_prompt):
    # Call the QWen API with the prompt
    response = qwen.call(prompt)  
    usable_response = response.strip()  # Strip any leading/trailing whitespace
    return usable_response