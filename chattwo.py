import cohere
import json
import os

co = cohere.ClientV2("lZGOc9ZynZ67K87qUOVCe60Z4BNDprTSynb1BaIh")


def load_conversation(phone_number):
    filename = f"{phone_number}.json"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    else:
        return []

def save_conversation(phone_number, messages):
    filename = f"{phone_number}.json"
    with open(filename, "w") as f:
        json.dump(messages, f, indent=2)



def chat(message):
    response = co.chat(
        model="command-a-03-2025", 
        messages=[{"role": "user", "content": f"keep your response under 165 Characters, answer: {message}"}],
        max_tokens=160,
    )
    answer= response.message.content[0].text
    return answer


def chatold(message,phone_number):
    messages = load_conversation(phone_number)
    messages.append({"role": "user", "content": message})
    response = co.chat(
        model="command-a-03-2025", 
        messages=[{"role": "user", "content": f"{messages}"}],
        max_tokens=160,
    )
    answer= response.message.content[0].text
    messages.append({"role": "assistant", "content": answer})
    # Save conversation
    save_conversation(phone_number, messages)
    print(response.message.content[0].text)
    return answer

def chat_with_speech(message):
    answer = ""
    if message == "":
        answer = "Please say something."
    else:
        response = co.chat(
            model="command-a-03-2025", 
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=100,
        )
        answer= response.message.content[0].text
        print(answer)
    return answer

