my_bot_rules = {
    "hello": "Welcome to my chatbot! How can I help you?",
    "how are you": "I am fine, thanks for asking! How about you?",
    "what is your domain": "This is a rule-based AI project for my internship.",
    "who created you": "I was created by Moaaz in 2026.",
    "help": "Options: hello, how are you, what is your domain, who created you, or exit."
}

print("--- Chatbot Started (Type 'exit' to stop) ---")

while True:
    user_text = input("User: ")
    clean_text = user_text.lower().strip()
    
    if clean_text == "exit":
        print("Goodbye!")
        break
        
    bot_reply = my_bot_rules.get(clean_text, "Sorry, I don't understand that. Type 'help' to see what I can do.")
    print("Bot:", bot_reply)