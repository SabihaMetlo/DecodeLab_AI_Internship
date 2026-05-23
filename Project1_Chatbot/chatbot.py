print("AI Chatbot Started!")
print("Type 'bye' to exit.\n")

while True:

    user = input("You: ").lower()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hi there!")
        
    elif user == "how are you":
        print("Bot: I am fine!")

    elif user == "what is your name":
        print("Bot: I am a rule-based AI chatbot.")

    elif user == "favorite color":
        print("Bot: I like blue.")

    elif user == "time":
        print("Bot: I cannot check real time yet.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")