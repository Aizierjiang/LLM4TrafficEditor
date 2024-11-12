import config as config
import openai

openai.api_key = config.api_key

prompt = '''
Give me an introduction of computer graphics.
'''

response = openai.Completion.create(model="text-davinci-003",
                                    prompt=prompt,
                                    max_tokens=100,
                                    temperature=0)

print(response)
print("-------------------------")
print(response['choices'][0]['text'])

'''
Printed result:

{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "text": "\nComputer graphics is the field ... "
    }
  ],
  "created": 1680935958,
  "id": "cmpl-xxxxxxx",
  "model": "text-davinci-003",
  "object": "text_completion",
  "usage": {
    "completion_tokens": 97,
    "prompt_tokens": 10,
    "total_tokens": 107
  }
}
-------------------------

Computer graphics is the field of ... 
'''