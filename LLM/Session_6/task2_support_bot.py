"""
Session 6 - Task 2: Customer Support Chatbot for a food delivery app (Zomato/Swiggy style)
Handles 3 types of queries with if-else logic: order status, refund request, delivery delay.
Run: python task2_support_bot.py
"""


def get_reply(user_input: str) -> str:
    text = user_input.lower().strip()

    # 1) Order status
    if "order status" in text or "where is my order" in text or "track" in text or "status" in text:
        return ("Your order is being prepared by the restaurant and will be picked up soon. "
                "You can also track it live on the 'My Orders' page.")

    # 2) Refund request
    elif "refund" in text or "money back" in text or "wrong item" in text or "cancel" in text:
        return ("Sorry for the trouble! Your refund request has been noted. "
                "The amount will be credited to your original payment method within 5-7 working days.")

    # 3) Delivery delay
    elif "delay" in text or "late" in text or "not delivered" in text or "taking too long" in text:
        return ("We are sorry your order is late. Your delivery partner is on the way and "
                "should reach you in about 10-15 minutes. Thank you for your patience!")

    elif text in ("hi", "hello", "hey"):
        return "Hello! I can help with order status, refund requests and delivery delays."

    else:
        return ("Sorry, I did not understand that. Please type one of these: "
                "'order status', 'refund', or 'delivery delay'.")


def main():
    print("=== FoodieBot Customer Support ===")
    print("Type 'exit' to quit.\n")
    while True:
        user = input("You: ")
        if user.lower().strip() in ("exit", "quit", "bye"):
            print("Bot: Thank you for contacting us. Have a great day!")
            break
        print("Bot:", get_reply(user), "\n")


if __name__ == "__main__":
    main()
