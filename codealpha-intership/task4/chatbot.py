
"""
CodeAlpha Internship - Task 4
Project: Basic Rule-Based Chatbot

Author: B V N SAI SHRESHTAN
Description:
    A simple rule-based chatbot that interacts with the user
    using predefined responses.
"""

from datetime import datetime


class ChatBot:
    """A simple rule-based chatbot."""

    def __init__(self):
        self.name = "CodeAlpha Bot"

        self.responses = {
            "hello": [
                "Hello! 👋 How can I help you?",
                "Hi there! Nice to meet you!",
                "Hey! How are you doing?"
            ],
            "hi": [
                "Hi! 👋 How can I help you?",
                "Hello! What can I do for you?"
            ],
            "how are you": [
                "I'm doing great! Thanks for asking.",
                "I'm fine, thanks! How about you?"
            ],
            "what is your name": [
                "I'm CodeAlpha Bot, your simple Python assistant."
            ],
            "who are you": [
                "I'm a rule-based chatbot created using Python."
            ],
            "help": [
                "I can respond to greetings, answer basic questions, "
                "tell the current time, and end the conversation."
            ],
            "thank you": [
                "You're welcome! 😊",
                "Happy to help!"
            ]
        }

    def get_response(self, message):
        """Generate a response based on the user's message."""

        message = message.lower().strip()

        for keyword, response_list in self.responses.items():
            if keyword in message:
                return response_list[0]

        if "time" in message:
            current_time = datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}."

        if message in {"bye", "exit", "quit"}:
            return "Goodbye! 👋 Have a great day!"

        return (
            "I'm sorry, I don't understand that yet. "
            "Try saying 'hello', 'help', or 'bye'."
        )


def display_welcome():
    """Display the chatbot welcome message."""

    print("=" * 60)
    print("             CODEALPHA BASIC CHATBOT")
    print("=" * 60)
    print("Type 'hello', 'help', 'what is your name', or 'bye'.")
    print("-" * 60)


def main():
    """Run the chatbot application."""

    chatbot = ChatBot()
    display_welcome()

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if not user_input:
                print("Bot: Please enter a message.")
                continue

            response = chatbot.get_response(user_input)

            print(f"Bot: {response}")

            if user_input.lower() in {"bye", "exit", "quit"}:
                break

        except KeyboardInterrupt:
            print("\n\nBot: Goodbye! 👋")
            break

        except Exception as error:
            print(f"Bot: An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()