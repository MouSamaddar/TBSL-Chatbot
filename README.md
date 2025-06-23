# TBSL-Chatbot

A smart virtual assistant built for **Tata BlueScope Steel** using **Streamlit**, enabling real-time interaction through voice and text. This chatbot answers queries related to safety protocols, HR policies, operations, and more—offering an intuitive, responsive, and interactive experience for users within the organization.

---

### 🚀 Features

* Real-time response display with query history
* NLP-powered intelligent query handling
* Dynamic map embedding for location-based responses
* Fully interactive and user-friendly UI
* Custom theme toggling and animated backgrounds
* Keyword and intent-based search with personalized replies

---

### 🧠 Tech Stack

| Tool/Library      | Purpose                        |
| ----------------- | ------------------------------ |
| Python            | Core programming language      |
| Streamlit         | Frontend web interface         |
| SpeechRecognition | Capturing and converting voice |
| pyttsx3           | Text-to-speech for responses   |
| OpenAI/Custom NLP | Natural Language Processing    |
| SQLite/MySQL      | Storing knowledge base         |
| HTML/CSS/JS       | Enhancing UI responsiveness    |

---

### 💬 Supported Interactions

| Input Type                | Functionality                          |
| ------------------------- | -------------------------------------- |
| Text input                | General and specific queries           |
| Voice input (mic)         | Hands-free communication               |
| "Safety guidelines"       | Returns safety-related content         |
| "HR policies"             | Shows HR documents and links           |
| "Plant location"          | Displays embedded location map         |
| "Contact support"         | Provides contact details or email form |
| Theme toggle              | Switch between light and dark modes    |
| "Exit" or "Close" command | Ends the chatbot session gracefully    |

---

### 🏗️ How It Works

The chatbot uses **Streamlit** to render a sleek web interface where users can type or speak their queries. Voice inputs are converted to text using `SpeechRecognition` and processed through NLP logic to match relevant answers from the database. The system supports both predefined questions and adaptive keyword responses.

---

### 📦 Setup Instructions

1. Clone the repository
2. Install dependencies:

   ```bash
   pip install -r requirements.txt  
   ```
3. Run the Streamlit app:

   ```bash
   streamlit run chatbot.py  
   ```



