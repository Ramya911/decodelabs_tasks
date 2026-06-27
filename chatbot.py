# ============================================================
#  Rule-Based Chatbot
#  Skills: Control Flow · Decision-Making Logic · Basic AI
# ============================================================

def get_response(user_input):
    """
    Core decision engine — pure if-else logic.
    Checks the user's message against predefined rules
    and returns the matching response.
    """
    text = user_input.lower().strip()

    # ── Greetings ────────────────────────────────────────────
    if text in ["hello", "hi", "hey", "howdy", "sup"]:
        return "Hello! 👋 How can I help you today?"

    elif "good morning" in text:
        return "Good morning! ☀️ Hope you have a great day!"

    elif "good night" in text:
        return "Good night! 🌙 Sweet dreams!"

    # ── Bot identity ─────────────────────────────────────────
    elif "your name" in text or "who are you" in text:
        return "I'm RuleBot 🤖 — a simple rule-based chatbot built with if-else logic!"

    elif "how are you" in text or "how're you" in text:
        return "I'm doing great, thanks for asking! I'm powered by pure if-else — no bad days here 😄"

    # ── Help ─────────────────────────────────────────────────
    elif text in ["help", "commands", "options"]:
        return (
            "I understand:\n"
            "  • Greetings     → hello, hi, hey, good morning, good night\n"
            "  • About me      → who are you, your name, how are you\n"
            "  • Fun           → joke, fun fact\n"
            "  • Utility       → time, date\n"
            "  • Exit          → bye, quit, exit\n"
            "Type 'help' anytime to see this list."
        )

    # ── Jokes ────────────────────────────────────────────────
    elif "joke" in text:
        return "Why do programmers prefer dark mode?\nBecause light attracts bugs! 🐛"

    elif "fun fact" in text:
        return "Fun fact: The first computer bug was an actual bug — a moth found in a Harvard Mark II relay in 1947! 🦋"

    # ── Utility ──────────────────────────────────────────────
    elif "time" in text:
        from datetime import datetime
        return f"Current time: {datetime.now().strftime('%H:%M:%S')} ⏰"

    elif "date" in text or "today" in text:
        from datetime import datetime
        return f"Today is {datetime.now().strftime('%A, %B %d, %Y')} 📅"

    # ── Gratitude ────────────────────────────────────────────
    elif text in ["thanks", "thank you", "thx", "cheers"]:
        return "You're welcome! 😊 Let me know if you need anything else."

    # ── Exit commands ────────────────────────────────────────
    elif text in ["bye", "goodbye", "exit", "quit", "see you", "cya"]:
        return "EXIT"   # sentinel value caught by the main loop

    # ── Fallback (else branch) ───────────────────────────────
    else:
        return (
            f"Sorry, I don't understand '{user_input}'.\n"
            "Type 'help' to see what I can respond to."
        )


# ── Main loop ────────────────────────────────────────────────
def main():
    print("=" * 45)
    print("   Welcome to RuleBot 🤖")
    print("   A simple rule-based chatbot")
    print("   Type 'help' for commands | 'quit' to exit")
    print("=" * 45)

    # Continuous loop — keeps the chatbot running until exit
    while True:
        try:
            user_input = input("\nYou: ").strip()

            # Skip empty input
            if not user_input:
                print("Bot: Please type something!")
                continue

            response = get_response(user_input)

            # Exit command detected
            if response == "EXIT":
                print("Bot: Goodbye! 👋 See you next time!")
                break  # exit the loop

            print(f"Bot: {response}")

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\nBot: Interrupted. Goodbye! 👋")
            break


if __name__ == "__main__":
    main()
