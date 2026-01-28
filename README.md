# -AI-Chatbot-with-Gmail-n8n-
# 🤖 AI Chatbot with Gmail (n8n)

An AI-powered chatbot automation built using n8n, **OpenRouter / LLM, and **Gmail. This workflow listens to chat messages, generates intelligent responses using an AI Agent with memory and tools, and automatically sends replies via Gmail.

---

## 📸 Workflow Screenshot

<img width="1912" height="876" alt="emailchatbot" src="https://github.com/user-attachments/assets/37a73375-1bf3-413f-b3fb-6bf57996ef3c" />


## Output
<img width="1840" height="502" alt="Screenshot 2025-12-16 182040" src="https://github.com/user-attachments/assets/8888dd26-c9b9-4414-a18f-448c474b87ba" />



## 🔄 Workflow Overview

This automation enables real-time conversational AI integrated with email delivery.


User Chat Message
        │
        ▼
When Chat Message Received (Trigger)
        │
        ▼
AI Agent (LLM + Memory + Tools)
        │
        ▼
Gmail – Send Message (Reply)


---

## ⚙️ Nodes Explanation

### 1️⃣ When Chat Message Received

* Trigger node that activates when a user sends a chat message
* Acts as the entry point for the chatbot

---

### 2️⃣ AI Agent

The core intelligence of the system.

Connected Components:

* 🧠 Chat Model – OpenRouter Chat Model
* 💾 Simple Memory – Maintains conversation context
* 🔧 Tool – Wikipedia (for factual lookups)

Capabilities:

* Understands user queries
* Generates contextual responses
* Remembers previous messages
* Fetches information when required

---

### 3️⃣ Gmail – Send a Message

* Automatically sends the AI-generated response via Gmail
* Can be used for:

  * Support replies
  * Code explanations
  * Knowledge-based responses

---

## 📤 Sample Chat Output

User Input:


i want python code in add two numbers


AI Response:

python
# Function to add two numbers

def add_numbers(num1, num2):
    return num1 + num2

# Example usage
number1 = 5
number2 = 10
result = add_numbers(number1, number2)
print("The sum of", number1, "and", number2, "is:", result)


This response is automatically sent to the user via Gmail.

---

## 🧰 Tech Stack

* n8n – Workflow Automation
* OpenRouter LLM – AI Chat Model
* Simple Memory – Conversation context
* Wikipedia Tool – Knowledge retrieval
* Gmail API – Email delivery

---

## 🚀 Key Features

* ✅ Real-time AI chatbot
* ✅ Memory-enabled conversations
* ✅ Tool-augmented responses
* ✅ Automatic Gmail replies
* ✅ No-code / low-code automation

---

## 📂 Repository Structure


├── README.md
├── screenshots/
│   └── ai-chatbot-gmail-workflow.png
├── outputs/
│   └── sample-chat-response.txt


---

## 📌 Use Cases

* AI Email Assistant
* Customer Support Bot
* Coding Helpdesk
* Knowledge-based Chatbot
* Gmail Automation

---

## 👨‍💻 Author

Ashwini Pawar
AI | Data Analyst | Automation Builder

---

⭐ If you found this project useful, please star the repository and feel free to fork!
