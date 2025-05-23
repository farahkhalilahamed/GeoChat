from openai import OpenAI

client = OpenAI()

user_input = input("\nAsk something...\n")

model = "gpt-3.5-turbo"
messages = [
    {"role": "system", "content": "You are a fun assistant that knows a lot about geography."},
    {"role": "user", "content": user_input}
]
response = client.chat.completions.create(
    model = model,
    messages = messages
)

user_response = response.choices[0].message.content
print("\n" + user_response + "\n")