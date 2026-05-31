import os
import google.generativeai as genai

# Configure the Google Generative AI SDK with your API key.
# For a "long-lived" agent, consistent access to the AI service is essential.
# Ensure your GOOGLE_API_KEY environment variable is set.
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable not set. Please set it before running.")
genai.configure(api_key=API_KEY)

# Initialize the Generative Model, e.g., 'gemini-pro' for text generation.
model = genai.GenerativeModel('gemini-pro')

# Start a chat session. The `start_chat` method automatically manages
# the conversation history, which is key to creating a "long-lived" agent
# that remembers previous interactions within the session.
chat = model.start_chat(history=[])

print("Yapay Zeka Ajanı ile Sohbet (Çıkmak için 'çık' yazın)\n")
print("--------------------------------------------------")

# Simulate a conversation loop to demonstrate the agent's memory.
while True:
    user_message = input("Siz: ")
    if user_message.lower() == 'çık':
        break

    try:
        # Send the user's message to the model. The `chat` object automatically
        # includes the entire conversation history with each new message,
        # allowing the agent to provide context-aware responses.
        response = chat.send_message(user_message)
        print(f"Ajan: {response.text}")

        # The agent's "memory" (chat.history) grows with each turn.
        # This allows it to build on previous statements and maintain context,
        # simulating a "long-lived" interaction.
        # Uncomment the following lines to see the full history being maintained:
        # print("\n--- Mevcut Sohbet Geçmişi ---")
        # for message in chat.history:
        #     print(f"  {message.role}: {message.parts[0].text}")
        # print("------------------------------\n")

    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        print("Lütfen GOOGLE_API_KEY'inizin doğru ayarlandığından ve API erişiminizin olduğundan emin olun.")
        break

print("\nSohbet sona erdi.")
