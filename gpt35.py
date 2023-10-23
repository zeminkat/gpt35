import openai

openai.api_key = "API_KEY"  
print("ChatGPT: Selam Paşa! Ben gpt nasıl yardımcı olabilirim?")
messages = [
   
    {"role": "system", "content": "Hi ChatGPT, You are a helpful assistant!"},
]
while True:
    soru=input("Sorunuz:  ")
    messages.append({"role":"system","content":soru})
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat_completion["choices"][0]["message"]["content"]
    print(reply)
    messages.append({"role": "assistant", "content": reply})
