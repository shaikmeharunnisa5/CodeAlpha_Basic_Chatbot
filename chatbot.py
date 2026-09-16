def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi!"

    elif "how are you" in user_input:
        return "I'm fine, thanks!"

    elif "bye" in user_input:
        return "Goodbye!"

    else:
        return "Sorry, I don't understand."


print("Welcome to the Basic Chatbot!")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    if "bye" in user_input.lower():
        print("Chatbot:", get_response(user_input))
        break
    else:
        print("Chatbot:", get_response(user_input))