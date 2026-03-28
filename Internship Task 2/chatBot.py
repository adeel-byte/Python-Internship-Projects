def chatbot():
    print("Chatbot: Hello! I am your simple chatbot.")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Chatbot: Hello!")

        elif user == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Chatbot: I'm chatbot programmed by Adeel.")

        elif user == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")

chatbot()