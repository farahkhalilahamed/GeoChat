from openai import OpenAI

client = OpenAI()

def set_user_input_category(user_input):
    question_keywords = ["who", "what", "when", "where", "why", "how", "?"]
    for keyword in question_keywords:
        if keyword in user_input.lower():
            return "question"
    return "statement"

def get_response(model, messages):
    # api call
    api_response = client.chat.completions.create(
        model = model,
        messages = messages
    )
    
    # extract text from api call
    response = api_response.choices[0].message.content
    return response


user_input = input("\nAsk me something about geography!\n")

model = "gpt-3.5-turbo"
messages = [
    {"role": "system", "content": "You are a fun assistant that loves geography."},
    {"role": "user", "content": user_input}
]

user_response = get_response(model, messages)
if set_user_input_category(user_input) == "question":
    user_response = "Good question! " + user_response

print("\n" + user_response + "\n")
