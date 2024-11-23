# Gemini Chatbot | Streamlit

![Gemini Chatbot](Demo.mp4)

## Overview 

This project is a Streamlit-based chat application that interacts with the Gemini AI model, allowing users to engage in conversations with an artificial intelligence assistant. The application stores chat history, allowing users to revisit and continue previous conversations.

## Features
- **Chat Interface**: Engage in real-time conversations with the AI assistant.
- **Chat History**: Save and revisit past chats.
- **User-Friendly Design**: Simple and intuitive interface built with Streamlit.
- **Environment Variable Management**: Securely manage API keys using dotenv.

## Technologies Used
- **Python**: The primary programming language for development.
- **Streamlit**: For building the user interface.
- **Google Gemini API**: For chat functionality, which drives from Gemini model.
- **dotenv**: For managing environment variables.
- **html & css**: For managing visuality of the web structure using markdown.

## Getting Started

### Dependencies

This code uses the following libraries:

- `streamlit`: for building the user interface.
- `google.generativeai`: for chat functionality.
- `python-dotenv`: for managing environment variables.
- Gemini API key: Get it from [Google AI Studio](https://ai.google.dev/tutorials/setup?hl=tr).

## Contributing

We welcome contributions to enhance the Gemini Chatbot Interface! Here’s how you can get involved:

### How to Contribute
1. **Fork the Repository**: Click on the "Fork" button at the top right of this page.
2. **Clone Your Fork**: Clone your forked repository to your local machine.
   ```bash
   git clone https://github.com/AlexKalll/Advanced-Gemini-Powered-ChatGPT.git

### Usage

Follow these steps to set up and run the project:
- **Initially Clone the repository:**
   ```bash
   git clone https://github.com/AlexKalll/Advanced-Gemini-Powered-ChatGPT.git

1. **Create a virtual environment:**
   ```bash
   python3 -m venv my_env
   source my_env/bin/activate 
   # For Windows
   .\my_env\Scripts\activate 
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Run the Streamlit server:**
   ```bash
   streamlit run app_chat.py
4. **Access the application in your browser at http://localhost:8501.**

4. **Start chatting with the assistant!**
- ### Repository Structure
   ```bash
   repository/
   ├── app_chat.py               # the code and UI integrated together live here
   ├── requirements.txt          # the python packages needed to run locally
   ├── .streamlit/
   │   └── config.toml           # theme info for the UI
   ├── data/                     # folder for saved chat messages 
   ├── Demo.gif                  # demo of the bot                    
## How it Works
1. The user enters a question in the input field.
2. User messages are sent to the Gemini model for processing.
3. The user's input, along with the chat history, is used to generate a response.
4. The Gemini model generates a response based on the patterns it learned during training.
5. The application saves chat messages and Gemini AI chat history to files for later retrieval.
6. A new chat is created if the user initiates a conversation that hasn't been stored before, or the user can go back to past chats.

Contact Me for any inquiries or feedback.

[LinkedIn](https://www.linkedin.com/in/kaletsidik-ayalew-mekonnen-34772226b/) | [Instagram](https://www.instagram.com/kaletsidik.24?igsh=YzljYTk1ODg3Zg==) | [X~Twitter](https://x.com/kaletsidike?t=VCe79O084EmE9bM2V5jOIA&s=09) | [Telegram](https://t.me/Adragon_de_mello) | [GitHub](https://github.com/AlexKalll) | [LeetCode](https://leetcode.com/Alexkal/)


Kaletsidik Ayalew
alexkalalw@gmail.com