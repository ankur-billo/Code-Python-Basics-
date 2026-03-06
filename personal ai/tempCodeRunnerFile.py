
import os
from openai import OpenAI

key="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"

messages=[]

client = OpenAI(
    # This is the default and can be omitted
    api_key=key,
)

def completion(message):
    global messages;
    messages.append(
        {
            "role": "user",
            "content": message,
        },
   )
    
    chat_completion = client.chat.completions.create(messages=messages,
    model="gpt-5.2"
)

print(chat_completion)

if __name__ == "__main__":
    user_question = input("Hi, I'm your Sebak. Hpow can I saheta you?:\n")
    completion(user_question)
