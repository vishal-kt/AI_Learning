def chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi there! 😊"
    elif "how are you" in user_input:
        return "I am just code, but I feel intelligent!"
    elif "ai" in user_input:
        return "AI is fascinating, isn't it?"
    else:
        return "Tell me more..."

while True:
    msg = input("You: ")
    if msg == "exit":
        break
    print("Bot:", chatbot(msg))