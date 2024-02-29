from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
!pip install openai

import openai

api_key = ""
openai.api_key = api_key

def generate_music_from_text_api(text_prompt):
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=text_prompt,
        max_tokens=1000,
        n=1, 
        temperature=0.7
    )
    music_sequence = response.choices[0].text.strip()
    return music_sequence
text_prompt = "A joyful tune for our new product launch!"
music_sequence_api = generate_music_from_text_api(text_prompt)
