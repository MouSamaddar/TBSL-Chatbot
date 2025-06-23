# TBSL-Chatbot
The TBSL Chatbot is a smart virtual assistant designed for Tata BlueScope Steel using Streamlit. It provides quick, voice-enabled responses to user queries and supports dynamic map embedding and real-time interaction. Powered by NLP models, it handles safety, HR, and operational queries efficiently, offering a smooth and responsive user experience.

🚀 Features
Real-time response display with query history

NLP-powered intelligent query handling

Dynamic map embedding for location-based responses

Fully interactive and user-friendly UI

Custom theme toggling and animated backgrounds

Keyword and intent-based search with personalized replies

🧠 Tech Stack
Tool/Library	Purpose
Python	Core programming language
Streamlit	Frontend web interface
SpeechRecognition	Capturing and converting voice
pyttsx3	Text-to-speech for responses
OpenAI/Custom NLP	Natural Language Processing
SQLite/MySQL	Storing knowledge base
HTML/CSS/JS	Enhancing UI responsiveness

💬 Supported Interactions
Input Type	Functionality
Text input	General and specific queries
Voice input (mic)	Hands-free communication
"Safety guidelines"	Returns safety-related content
"HR policies"	Shows HR documents and links
"Plant location"	Displays embedded location map
"Contact support"	Provides contact details or email form
Theme toggle	Switch between light and dark modes
"Exit" or "Close" command	Ends the chatbot session gracefully

🏗️ How It Works
The chatbot uses Streamlit to render a sleek web interface where users can type or speak their queries. Voice inputs are converted to text using SpeechRecognition and processed through NLP logic to match relevant answers from the database. The system supports both predefined questions and adaptive keyword responses.

📦 Setup Instructions
Clone the repository

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt  
Run the Streamlit app:

bash
Copy
Edit
streamlit run tbsl_chatbot.py  
