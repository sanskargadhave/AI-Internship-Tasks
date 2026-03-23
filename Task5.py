import tkinter as tk

# -------------------------------
# Step 1: Chatbot Logic
# -------------------------------
def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi Sanskar!"
    elif user_input == "how are you":
        return "I am fine!"
    elif user_input == "your name":
        return "I am AI Bot"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand"

# -------------------------------
# Step 2: Send Message Function
# -------------------------------
def send_message():
    user_text = entry.get()

    if user_text.strip() == "":
        return

    chat_area.insert(tk.END, "You: " + user_text + "\n")

    bot_reply = chatbot_response(user_text)
    chat_area.insert(tk.END, "Bot: " + bot_reply + "\n\n")

    entry.delete(0, tk.END)

# -------------------------------
# Step 3: GUI Setup
# -------------------------------
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("400x500")

# Chat display area
chat_area = tk.Text(root, height=20, width=50)
chat_area.pack(pady=10)

# Input field
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Send button
send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack()

# -------------------------------
# Step 4: Run App
# -------------------------------
root.mainloop()