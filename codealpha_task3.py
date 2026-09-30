def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "bye":
        return "Goodbye!"

    elif user_input == "what is your name":
        return "I'm a simple Python chatbot."

    elif user_input == "help":
        return "You can say: hello, how are you, what is your name, or bye."

    else:
        return "Sorry, I don't understand that."


def chatbot():
    print("===== Simple Chatbot =====")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("\nYou: ")

        response = chatbot_response(user_input)

        print("Bot:", response)
        if user_input.lower() == "bye":
            break


# Start the chatbot
chatbot()